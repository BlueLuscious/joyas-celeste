// export class MessageService {

//     /**
//     * Show Messages:
//     * 
//     * Use Unicorn to call methods, show django messages.
//     * @param {string} level Level Tag.
//     * @param {string} message Text Message.
//     * @returns {Promise<void>} None.
//     */
//     static async addMessage(level, message) {
//         console.log(`Message: ${message} - Level Tag: ${level}`)
//         Unicorn.call("django-messages", "add_message", level, message)

//     }


//     /**
//     * Hide Messages:
//     * 
//     * Use Unicorn to call methods, hide django messages.
//     * @param {string} message Text Message.
//     * @returns {void} None.
//     */
//     static removeMessage(message = "") {
//         if (message != "") {
//             console.log(`Remove message: ${message}`)
//         }
//         setTimeout(() => {
//             Unicorn.call("django-messages", "remove_message", message)
//         }, 4000)
//     }

// }
