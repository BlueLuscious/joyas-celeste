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
     * @param {string} classlist Classlist.
     * @returns {void} None.
     */
    openSideNavbarByClick(buttons, element, classlist) {
        buttons.forEach(button => {
            button.addEventListener("click", () => {
                element.classList.toggle(classlist)
            })
        })
    }

}
