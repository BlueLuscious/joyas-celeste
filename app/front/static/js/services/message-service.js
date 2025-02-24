export class MessageService {

    /**
    * Show Django Messages:
    * 
    * Use Unicorn to call methods, show django message.
    * @returns {void} None.
    */
    static addDjangoMessage() {
        Unicorn.call("django-messages", "add_django_message")
    }


    /**
    * Show Messages:
    * 
    * Use Unicorn to call methods, show message.
    * @param {int} level Message Level (Default `0`).
    * @param {string} text Text Message (Default `""`).
    * @returns {void} None.
    */
    static addMessage(level = 0, text = "") {
        Unicorn.call("django-messages", "add_message", level, text)
    }


    /**
    * Remove Messages:
    * 
    * Use Unicorn to call methods, remove message.
    * @returns {void} None.
    */
    static removeMessage() {
        Unicorn.call("django-messages", "remove_message")
    }
    
}
