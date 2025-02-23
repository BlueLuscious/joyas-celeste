import { Helpers } from "../helpers/helpers.js";


export class MessageService {

    /**
    * Display Messages:
    * 
    * Use Unicorn to call methods, display django messages.
    * @returns {Promise<void>} None.
    */
    static async displayMessages() {
        await Helpers.unicornCallAsync("django-messages", "add_message")
    }


    /**
    * Hide Messages:
    * 
    * Use Unicorn to call methods, hide django messages.
    * @returns {Promise<void>} None.
    */
    static async hideMessages() {
        setTimeout(async () => {
            await Helpers.unicornCallAsync("django-messages", "remove_message")
        }, 3500)
    }
}
