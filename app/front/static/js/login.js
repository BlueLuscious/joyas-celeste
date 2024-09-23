import { Helpers } from "./helpers/helpers.js"

const Helper = new Helpers()

document.addEventListener("DOMContentLoaded", () => {

    /* Send Form */
    const logInButton = document.getElementById("log_in_button")
    const loginForm = document.getElementById("login_form")
    
    logInButton.addEventListener("click", (event) => {
        event.preventDefault()

        if (loginForm.checkValidity()) {
            loginForm.submit()
        } else {
            loginForm.reportValidity()
        }
    })


    /* Toggle Password */
    const passwordToggle = document.getElementById("toggle_password")
    const passwordInput = document.getElementById("id_password")
    const eyeIcon = document.getElementById("eye_icon")
    const eyeSlashIcon = document.getElementById("eye_slash_icon")

    passwordToggle.addEventListener("click",  () => {
        Helper.toggleDisplayPassword(passwordInput, eyeIcon, eyeSlashIcon)
    })

})
