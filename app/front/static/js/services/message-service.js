export class MessageService {

    /**
    * Display Messages:
    * 
    * Use Unicorn to call methods, display django messages.
    * @returns {void} None.
    */
    static displayMessages() {
        Unicorn.call("django-messages", "add_message")

        setTimeout(() => {
            Unicorn.call("django-messages", "remove_message")
        }, 4000)
    }

}
