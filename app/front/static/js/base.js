document.addEventListener("DOMContentLoaded", () => {

    const menu = document.getElementById("menu")
    const closeMenu = document.getElementById("close_menu")
    const sideNavbar = document.getElementById("side_navbar")
    const sideNavbarButtons = [menu, closeMenu]

    sideNavbarButtons.forEach(button => {
        button.addEventListener("click", () => {
            sideNavbar.classList.toggle("-translate-x-full")
        })
    })

})
