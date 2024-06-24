export class WhatsappService {

    openWhatsApp() {
        const phoneNumber = 5493364581618
        window.open(`https://wa.me/${phoneNumber}`, "_blank")
    }

}
