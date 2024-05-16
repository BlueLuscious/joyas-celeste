document.addEventListener("DOMContentLoaded", () => {

    const menu = document.getElementById("menu")
    const closeMenu = document.getElementById("close_menu")
    const leftSideNavbar = document.getElementById("left_side_navbar")
    const leftSideNavbarButtons = [menu, closeMenu]

    openSideNavbar(leftSideNavbarButtons, leftSideNavbar, "-translate-x-full")

    const cart = document.getElementById("cart")
    const closeCart = document.getElementById("close_cart")
    const rightSideNavbar = document.getElementById("right_side_navbar")
    const rightSideNavbarButtons = [cart, closeCart]

    openSideNavbar(rightSideNavbarButtons, rightSideNavbar, "translate-x-full")

})

function openSideNavbar(buttons, element, classlist) {
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            element.classList.toggle(classlist)
        })
    })
}
