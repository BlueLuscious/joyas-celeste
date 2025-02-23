import { Helpers } from "../helpers/helpers.js";
import { MessageService } from "./message-service.js";


export class ShoppingCartService {

    /**
    * Add item to shopping cart:
    * 
    * Use Unicorn to call methods, add an item to cart and update cart counter.
    * @param {string} product_uuid Product UUID.
    * @returns {void}  None.
    */
    static async addToCart(product_uuid) {
        let product_size = document.getElementById(product_uuid);

        if (!product_size) {
            reject(new Error("El elemento de tamaño del producto no existe."));
        }

        try {
            await Helpers.unicornCallAsync("shopping-cart", "add_to_cart", product_uuid, product_size.value)
            await ShoppingCartService.updateCartCounter();
            await MessageService.displayMessages();
            await MessageService.hideMessages();

        } catch (error) {
            console.error("Error en addToCart:", error);
        }
    }


    /**
    * Update shopping cart counter:
    * 
    * Use Unicorn to call methods, update shopping cart counter.
    * @returns {Promise<void>} None.
    */
    static async updateCartCounter() {
        await Helpers.unicornCallAsync("shopping-cart-counter", "update_cart_counter")
    }

}
