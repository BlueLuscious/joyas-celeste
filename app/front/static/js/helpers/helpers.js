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

    /**
     * Toggle Display Password:
     * @param {Object} password_input Input.
     * @param {Object} eye_icon Eye Icon.
     * @param {Object} eye_slash_icon Eye Slash Icon.
     * @returns {void} None.
     */
    toggleDisplayPassword(password_input, eye_icon, eye_slash_icon) {
        const isPassword = password_input.type === "password"
        password_input.type = isPassword ? "text" : "password"

        eye_icon.classList.toggle("hidden", isPassword)
        eye_slash_icon.classList.toggle("hidden", !isPassword)
    }

}
