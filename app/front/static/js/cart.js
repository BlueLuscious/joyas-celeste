import { CartService } from "./services/cart-service.js"
const cart_service = new CartService

document.addEventListener("DOMContentLoaded", function() {

    const addToCartButtons = document.querySelectorAll('[id^="add_to_cart_"]')
    cart_service.addProduct(addToCartButtons)
    
    const deleteButtons = document.querySelectorAll('.delete_item')
    cart_service.removeProduct(deleteButtons)

})
