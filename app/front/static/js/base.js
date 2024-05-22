document.addEventListener("DOMContentLoaded", () => {

    /* LEFT SIDE NAVBAR */
    /* Expand Menu */
    const menu = document.getElementById("menu")
    const closeMenu = document.getElementById("close_menu")
    const leftSideNavbar = document.getElementById("left_side_navbar")
    const leftSideNavbarButtons = [menu, closeMenu]

    openSideNavbar(leftSideNavbarButtons, leftSideNavbar, "-translate-x-full")

    /* Expand Sub-Menus */
    const cardArrows = Array.from(document.getElementsByClassName("card_arrow"))
    const subMenus = Array.from(document.getElementsByClassName("sub_menu"))

    cardArrows.forEach((arrow, index) => {
        arrow.addEventListener("click", () => {
            cardArrows[index].classList.toggle("rotate-180")
            subMenus[index].classList.toggle("h-full")
            subMenus[index].classList.toggle("opacity-100")
            subMenus[index].classList.toggle("pb-4")
        })
    })

    /* RIGHT SIDE NAVBAR */
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
