export class ShoppingCartService {

    /**
    * Add item to shopping cart:
    * 
    * Use Unicorn to call methods, add an item to cart.
    * @param {string} product_uuid Product UUID.
    * @returns {void} None.
    */
    static addToCart(product_uuid) {
        console.log(`Product UUID: ${product_uuid}`)
        let product_size = document.getElementById(`product_${product_uuid}_size`)

        if (product_size) {
            console.log(`Product Size: ${product_size.value}`)
            Unicorn.call("shopping-cart", "add_to_cart", product_uuid, product_size.value)
        }
    }

}
