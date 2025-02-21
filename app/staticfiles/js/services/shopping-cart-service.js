export class ShoppingCartService {

    /**
    * Add item to shopping cart:
    * 
    * Use Unicorn to call methods, add an item to cart and update cart counter.
    * @param {string} product_uuid Product UUID.
    * @returns {void} None.
    */
    static addToCart(product_uuid) {
        console.log(`Product UUID: ${product_uuid}`)
        let form = document.getElementById(`product_form_${product_uuid}`)
        let formData = new FormData(form)
        for (let [key, value] of formData.entries()) {
            console.log(`${key}: ${value}`)
        }
        console.log([...formData.entries()])
        let product_size = formData.get("product_size")
        console.log(`Product Size: ${product_size}`)

        if (product_size) {
            Unicorn.call("shopping-cart", "add_to_cart", product_uuid, product_size)
        }
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

}
