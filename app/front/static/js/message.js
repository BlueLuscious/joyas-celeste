import { MessageService } from "./services/message-service.js"

window.addMessage = MessageService.addMessage

document.addEventListener("DOMContentLoaded", () => {
    MessageService.addDjangoMessage()
})
