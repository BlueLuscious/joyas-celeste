export class Helpers {
    
    openSideNavbar(buttons, element, classlist) {
        buttons.forEach(button => {
            button.addEventListener("click", () => {
                element.classList.toggle(classlist)
            })
        })
    }
}
