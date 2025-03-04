export class MessageService {

    /**
    * Add Django Messages:
    * 
    * Use Unicorn to call methods, add django message.
    * @returns {void} None.
    */
    static addDjangoMessage() {
        Unicorn.call("django-messages", "add_django_message")
    }


    /**
    * Add Messages:
    * 
    * Use Unicorn to call methods, add message.
    * @param {int} level Message Level (Default `0`).
    * @param {string} text Text Message (Default `""`).
    * @returns {void} None.
    */
    static addMessage(level = 0, text = "") {
        Unicorn.call("django-messages", "add_message", level, text)
    }
    
}
