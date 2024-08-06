import { messageTemplate } from "../components/message.js"


export class Helpers {

    /**
     * Custom Request:
     * @param {string} url URL.
     * @param {string} _method Method.
     * @param {json} _headers Headers.
     * @param {any} _body Body.
     * @returns {json} Response.
     */
    async customRequest(url, _method, _headers, _body = null) {
        return fetch(url, {
            method: _method,
            body: _body,
            headers: _headers
        })
        .then(response => response.json())
    }


    /**
    * Display Notification:
    * @param {string} message Message.
    * @param {string} type Message type.
    * @returns {void} None.
    */
    displayNotificationMessage(message, type) {
        const messageContainer = document.getElementById("message_container")

        const msg = document.createElement("div")
        msg.id = "message"
        msg.classList = "z-10 fixed top-24 flex justify-end w-full p-4 transform translate-x-full transition-transform duration-300 ease-in-out"
        msg.innerHTML = messageTemplate(message, type)
        messageContainer.appendChild(msg)

        setTimeout(() => {
            msg.classList.toggle("translate-x-full")
            setTimeout(() => {
                msg.classList.toggle("translate-x-full")
                setTimeout(() => {
                    msg.remove()
                }, 2300)
            }, 2200)
        }, 300)
    }


    /**
     * Format Number To Locale AR:
     * @param {number} number Number.
     * @returns {string} Formatted number.
     */
    formatNumberAR(number) {
        return number.toLocaleString(
            "es-AR", 
            { 
                style: "decimal", 
                minimumFractionDigits: 2, 
                maximumFractionDigits: 2, 
                useGrouping: true 
            }
        )
    }

   
    /**
     * Open Hide Navbar By Click Event:
     * @param {Array.<HTMLElement>} buttons Buttons.
     * @param {HTMLElement} element Element.
     * @param {HTMLElement} background Background element.
     * @param {string} classlist Classlist.
     * @returns {void} None.
     */
    openSideNavbarByClick(buttons, element, background, classlist) {
        buttons.forEach(button => {
            button.addEventListener("click", () => {
                element.classList.toggle(classlist)
                background.classList.toggle(classlist)
            })
        })
    }

}
