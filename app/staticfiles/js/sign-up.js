import { Helpers } from "./helpers/helpers.js"

window.toggleDisplayPassword = Helpers.toggleDisplayPassword

document.addEventListener("DOMContentLoaded", () => {

    /* Send Form */
    const signInButton = document.getElementById("sign_in_button")
    const signUpForm = document.getElementById("sign_up_form")
    
    signInButton.addEventListener("click", (event) => {
        event.preventDefault()

        if (signUpForm.checkValidity()) {
            signUpForm.submit()
        } else {
            signUpForm.reportValidity()
        }
    })

})
