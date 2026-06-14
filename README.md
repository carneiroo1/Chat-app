# 💬 Chat App

A real-time chat application built with Flask and Socket.IO, featuring user authentication, profile customization, and live messaging.

---

## ✨ Features

- 🔐 User registration and login with secure password hashing
- 💬 Real-time messaging with Socket.IO
- 🖼️ Profile pictures via URL
- 🔒 Session-based authentication
- 🚪 Logout support

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SocketIO
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Server:** Gunicorn + Gevent (production)
- **Deploy:** Render

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/carneiroo1/Chat-app.git
cd Chat-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root of the project:

```
SECRET_KEY=your-secret-key-here
```

### 5. Initialize the database

```bash
python init_db.py
```

### 6. Run the application

```bash
python app.py
```

Access it at `http://localhost:5000`

---

## 📁 Project Structure

```
Chat-app/
├── static/
│   ├── js/
│   │   └── chat.js
│   ├── chat.css
│   └── ...
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── chat.html
│   └── profile.html
├── app.py
├── init_db.py
├── requirements.txt
├── Procfile
└── .env.example
```

---

## 🌐 Live Demo

[https://chat-app-wqh2.onrender.com](https://chat-app-wqh2.onrender.com)

---

## 👤 Author

[@carneiroo1](https://github.com/carneiroo1)
