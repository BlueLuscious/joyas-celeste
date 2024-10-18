export class ShoppingCartService {

    /**
    * Add item to shopping cart:
    * 
    * Use Unicorn to call methods, add an item to cart and update cart counter.
    * @param {string} product_uuid Product UUID.
    * @returns {void} None.
    */
    static addToCart(product_uuid) {
        let form = document.getElementById(`product_form_${product_uuid}`)
        let formData = new FormData(form)
        let product_size = formData.get("product_size")

        if (product_size) {
            Unicorn.call("shopping-cart", "add_to_cart", product_uuid, product_size)
        }
    }


    /**
    * Remove item from shopping cart:
    * 
    * Use Unicorn to call methods, remove an item from cart and update cart counter.
    * @param {string} key Product UUID + Product size.
    * @returns {void} None.
    */
    static removeFromCart(key) {
        Unicorn.call("shopping-cart", "remove_from_cart", key)
    }


    /**
    * Update shopping cart counter:
    * 
    * Use Unicorn to call methods, update shopping cart counter.
    * @returns {void} None.
    */
    static updateCartCounter() {
        Unicorn.call("shopping-cart-counter", "update_cart_counter")
    }




    /**
    * Display Messages:
    * 
    * Use Unicorn to call methods, display django messages.
    * @returns {void} None.
    */
    static displayMessages() {
        Unicorn.call("django-messages", "display_messages")
    }

}
