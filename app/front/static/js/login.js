import { Helpers } from "./helpers/helpers.js"

window.toggleDisplayPassword = Helpers.toggleDisplayPassword

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

})
