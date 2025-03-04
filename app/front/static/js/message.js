import { MessageService } from "./services/message-service.js"

window.addDjangoMessage = MessageService.addDjangoMessage
window.addMessage = MessageService.addMessage
window.removeMessage = MessageService.removeMessage

document.addEventListener("DOMContentLoaded", () => {
    MessageService.addDjangoMessage()
})
