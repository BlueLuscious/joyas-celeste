import { MessageService } from "./services/message-service.js"

window.displayMessages = MessageService.displayMessages
window.hideMessages = MessageService.hideMessages

document.addEventListener("DOMContentLoaded", () => {
    MessageService.displayMessages()
})
