export class Helpers {
   
    /**
     * Open/Hide Navbar By Click Event:
     * @param {string} element_id Element ID.
     * @param {string} background_id Background element ID.
     * @param {string} classlist Classlist.
     * @returns {void} None.
     */
    static openSideNavbar(element_id, background_id, classlist) {
        const element = document.getElementById(element_id)
        const background = document.getElementById(background_id)
        element.classList.toggle(classlist)
        background.classList.toggle(classlist)
    }

    /**
     * Toggle Display Password:
     * @param {Object} password_input Input.
     * @param {Object} eye_icon Eye Icon.
     * @param {Object} eye_slash_icon Eye Slash Icon.
     * @returns {void} None.
     */
    static toggleDisplayPassword(password_input_id, eye_icon_id, eye_slash_icon_id) {
        const passwordInput = document.getElementById(password_input_id)
        const eyeIcon = document.getElementById(eye_icon_id)
        const eyeSlashIcon = document.getElementById(eye_slash_icon_id)

        const isPassword = passwordInput.type === "password"
        passwordInput.type = isPassword ? "text" : "password"

        eyeIcon.classList.toggle("hidden", isPassword)
        eyeSlashIcon.classList.toggle("hidden", !isPassword)
    }

    /**
     * Toggle the translate of an element:
     * @param {string} element_id Element ID.
     * @param {string} translate Tailwind Class.
     * @returns {void} None.
     */
    static toggleElementTranslateById(element_id, translate) {
        const element = document.getElementById(element_id)
        element.classList.toggle(translate)
    }

}
