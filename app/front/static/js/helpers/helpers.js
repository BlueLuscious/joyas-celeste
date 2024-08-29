export class Helpers {
   
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
