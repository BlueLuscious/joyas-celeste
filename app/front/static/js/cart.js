import { CartService } from "./services/cart-service.js"
const cart_service = new CartService

document.addEventListener("DOMContentLoaded", function() {

    const addToCartButtons = document.querySelectorAll('[id^="add_to_cart_"]')
    cart_service.addProduct(addToCartButtons)
    
    const removeFromCartButtons = document.querySelectorAll('[id^="remove_"]')
    cart_service.removeProduct(removeFromCartButtons)
    
    const subtractButtons = document.querySelectorAll('[id^="subtract_quantity_"]')
    const addButtons = document.querySelectorAll('[id^="add_quantity_"]')
    cart_service.updateQuantityProduct(subtractButtons, "subtract")
    cart_service.updateQuantityProduct(addButtons, "add")

})
