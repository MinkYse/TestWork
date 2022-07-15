let ws = new WebSocket("ws://localhost:8004/ws");
ws.onmessage = function(event) {
    let messages = document.getElementById('messages')
    let element = document.createElement('li')
    let data = JSON.parse(event.data)
    console.log(data.id)
    let content = document.createTextNode(data.message)
    element.appendChild(content)
    messages.appendChild(element)
};
function sendMessage(event) {
    let input = document.getElementById("messageText")
    ws.send(JSON.stringify({message: input.value}))
    input.value = ''
    event.preventDefault()
};