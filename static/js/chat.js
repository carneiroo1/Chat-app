const socket = io();

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("message").addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            enviarMensagem();
        }
    });
});

function enviarMensagem() {
    const input = document.getElementById("message");
    const message = input.value;
    if (message.trim() === "") return;
    socket.emit("send_message", {
        message: message,
        username: USERNAME
    });
    input.value = "";
}

socket.on("receive_message", function (data) {
    const list = document.getElementById("message-list");
    const item = document.createElement("li");
    item.innerHTML = `
        <div class="msg-box">
            <img src="${data.profile_picture}" alt="avatar" class="avatar">
            <div class="msg-content">
                <div class="msg-username"><strong><span>${data.username}</span></strong></div>
                <div class="msg-text"><span>${data.message}</span></div>
            </div>
        </div>
    `;
    list.appendChild(item);
});