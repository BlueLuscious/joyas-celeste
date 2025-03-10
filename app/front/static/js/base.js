import { Helpers } from "./helpers/helpers.js"
import { SocialNetworkService } from "./services/social-network-service.js"

window.openSideNavbar = Helpers.openSideNavbar
window.toggleElementTranslateById = Helpers.toggleElementTranslateById

window.openGoogleMaps = SocialNetworkService.openGoogleMaps
window.openInstagram = SocialNetworkService.openInstagram
window.openWhatsApp = SocialNetworkService.openWhatsApp

document.addEventListener("DOMContentLoaded", () => {

    /* LEFT SIDE NAVBAR */
    /* Expand Sub-Menus */
    const cardArrows = Array.from(document.getElementsByClassName("card_arrow"))
    const subMenus = Array.from(document.getElementsByClassName("sub_menu"))

    cardArrows.forEach((arrow, index) => {
        arrow.addEventListener("click", () => {
            cardArrows[index].classList.toggle("rotate-180")

            if (subMenus[index].classList.contains("max-h-0")) {
                subMenus[index].classList.remove("max-h-0", "opacity-0")
                subMenus[index].classList.add("max-h-full", "opacity-100")
            } else {
                subMenus[index].classList.remove("max-h-full", "opacity-100")
                subMenus[index].classList.add("max-h-0", "opacity-0")
            }
        })
    })

})
