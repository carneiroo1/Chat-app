const socket = io();

function sendMessage() {

    const input =
        document.getElementById("message");

    socket.emit(
        "send_message",
        {
            message: input.value
        }
    );

    input.value = "";
}
