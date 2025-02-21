export class SocialNetworkService {

    /**
    * Open WhatsApp.
    * @returns {void} None.
    */
    static openWhatsApp() {
        const phoneNumber = 5493364581618
        window.open(`https://wa.me/${phoneNumber}`, "_blank")
    }

    /**
    * Open Instagram.
    * @returns {void} None.
    */
    static openInstagram() {
        window.open("https://www.instagram.com/joyasceleste.longhi/", "_blank")
    }

    /**
    * Open Google Maps.
    * @returns {void} None.
    */
    static openGoogleMaps() {
        const latitude = -33.253801
        const longitude = -60.3725502
        window.open(`https://www.google.com/maps?q=${latitude},${longitude}`, "_blank")
    }

}
