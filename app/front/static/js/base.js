import { Helpers } from "./helpers/helpers.js"
import { WhatsappService } from "./services/whatsapp-service.js"

const Helper = new Helpers()
const WA_Service = new WhatsappService()

document.addEventListener("DOMContentLoaded", () => {

    /* LEFT SIDE NAVBAR */
    /* Expand Menu */
    const menu = document.getElementById("menu")
    const closeMenu = document.getElementById("close_menu")
    const leftSideNavbar = document.getElementById("left_side_navbar")
    const leftSideNavbarButtons = [menu, closeMenu]

    Helper.openSideNavbarByClick(leftSideNavbarButtons, leftSideNavbar, "-translate-x-full")

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

    Helper.openSideNavbarByClick(rightSideNavbarButtons, rightSideNavbar, "translate-x-full")

    /* FOOTER */
    const instagramRedirect = document.getElementById("instagram")
    const whatsappRedirect = document.getElementById("whatsapp")
    const whatsappButton = document.getElementById("whatsapp_button")
    const locationRedirect = document.getElementById("location")

    instagramRedirect.addEventListener("click", () => {
        window.open("https://www.instagram.com/joyasceleste.longhi/", "_blank")
    })

    whatsappRedirect.addEventListener("click", WA_Service.openWhatsApp)
    whatsappButton.addEventListener("click", WA_Service.openWhatsApp)

    locationRedirect.addEventListener("click", () => {
        const latitude = -33.253801
        const longitude = -60.3725502
        window.open(`https://www.google.com/maps?q=${latitude},${longitude}`, "_blank")
    })

})
