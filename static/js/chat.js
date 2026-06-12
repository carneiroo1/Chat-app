const socket = io();

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("message").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            enviarMensagem();
        }
    });
});

function enviarMensagem() {
    const input = document.getElementById("message");
    const message = input.value;
    if (message.trim() === "") return;
    socket.emit("send_message", { message: message });
    input.value = "";
}

// OUVINTE CORRIGIDO AQUI:
socket.on("receive_message", function(data) {
    const list = document.getElementById("message-list");
    const item = document.createElement("li");
    const strong = document.createElement("strong");
    strong.textContent = data.username;
    const br = document.createElement("br");
    const textoMensagem = document.createTextNode(` ${data.message}`);
    item.appendChild(strong);
    item.appendChild(br);
    item.appendChild(textoMensagem);
    list.appendChild(item);
});