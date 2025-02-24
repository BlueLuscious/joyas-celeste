export class MessageService {

    /**
    * Display Messages:
    * 
    * Use Unicorn to call methods, display django messages.
    * @param {int} level Message Level (Default `0`).
    * @param {string} text Text Message (Default `""`).
    * @returns {void} None.
    */
    static displayMessages(level = 0, text = "") {
        Unicorn.call("django-messages", "add_message", level, text)
    }


    /**
    * Hide Messages:
    * 
    * Use Unicorn to call methods, hide django messages.
    * @returns {void} None.
    */
    static hideMessages() {
        Unicorn.call("django-messages", "remove_message")
    }
}
