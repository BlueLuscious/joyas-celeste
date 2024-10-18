import { ShoppingCartService } from "./services/shopping-cart-service.js"

window.addToCart = ShoppingCartService.addToCart
window.removeFromCart = ShoppingCartService.removeFromCart
window.updateCartCounter = ShoppingCartService.updateCartCounter

window.displayMessages = ShoppingCartService.displayMessages
