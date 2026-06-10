function togglePassword() {

    const password =
        document.getElementById("password");

    const eye =
        document.getElementById("eye-icon");

    if (password.type === "password") {

        password.type = "text";
        eye.src = eye.dataset.closed;
        
    } else {
        
        password.type = "password";
        eye.src = eye.dataset.open;
    }
}x