from flask import Flask, render_template, request, redirect, session
import sqlite3
from flask_socketio import SocketIO, emit
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")

socketio = SocketIO(app)

@app.route('/')
def index():
    return redirect('/login')

@app.route("/register", methods=["GET", "POST"])
def register():
    username=""
    email=""
    password=""

    
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed = generate_password_hash(password)

        if not username or not email or not password:
            return render_template(
                "register.html",
                error="Please fill every container."
            )

        if len(password) < 8:
            return render_template(
                "register.html",
                error="Your password must have at least 8 digits."
            )
    
        if "@" not in email:
            return render_template(
                "register.html",
                error="Your email is in the wrong format."
            )
    


        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return render_template(
                "register.html",
                error="Esse nome de usuário já está em uso."
            )
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed)
        )

        conn.commit()
        conn.close()

        print(f"Usuário {username} cadastrado!")

    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    success = request.args.get("success")
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            return render_template(
                "login.html",
                error="Please fill every field."
            )

        if len(password) < 8:
            return render_template(
                "login.html",
                error="Password too small."
            )
    
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()
        if user and check_password_hash(user[3], password):
            session["username"] = username

            return redirect("/chat")
        
        else:
            return render_template(
                "login.html",
                error="User or password is wrong."
            )


    return render_template(
        "login.html",
        success=success,
    )

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

@app.route("/chat")
def chat():

    if "username" not in session:
        return redirect("/login")

    return render_template("chat.html")


@socketio.on("send_message")
def handle_message(data):
    emit("receive_message", data, broadcast=True)
    print(data["message"])

if __name__ == "__main__":
    socketio.run(app, debug=True)
