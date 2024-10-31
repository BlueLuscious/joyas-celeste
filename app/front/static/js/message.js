import { MessageService } from "./services/message-service.js"

window.displayMessages = MessageService.displayMessages

document.addEventListener("DOMContentLoaded", () => {
    MessageService.displayMessages()
})
