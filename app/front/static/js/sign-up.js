import { Helpers } from "./helpers/helpers.js"

const Helper = new Helpers()

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


    /* Toggle Password */
    const passwordToggle = document.getElementById("toggle_password")
    const passwordInput = document.getElementById("id_password")
    const eyeIcon = document.getElementById("eye_icon")
    const eyeSlashIcon = document.getElementById("eye_slash_icon")

    passwordToggle.addEventListener("click",  () => {
        Helper.toggleDisplayPassword(passwordInput, eyeIcon, eyeSlashIcon)
    })

})
