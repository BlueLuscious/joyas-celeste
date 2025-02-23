export class MessageService {

    /**
    * Display Messages:
    * 
    * Use Unicorn to call methods, display django messages.
    * @returns {void} None.
    */
    static displayMessages() {
        Unicorn.call("django-messages", "add_message")
    }


    /**
    * Hide Messages:
    * 
    * Use Unicorn to call methods, hide django messages.
    * @returns {void} None.
    */
    static hideMessages() {
        setTimeout(() => {
            Unicorn.call("django-messages", "remove_message")
        }, 3500)
    }
}
