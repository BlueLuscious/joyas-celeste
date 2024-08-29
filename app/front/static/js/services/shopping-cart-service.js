export class ShoppingCartService {

    static addToCart(product_uuid) {
        let form = document.getElementById("product_form_" + product_uuid)
        let formData = new FormData(form)
        let product_size = formData.get("product_size")

        Unicorn.call("shopping-cart", "add_to_cart", product_uuid, product_size)
        setTimeout(() => {
            Unicorn.call("shopping-cart-counter", "update_cart_counter")
        }, 100)
    }


    static removeFromCart(key) {
        Unicorn.call("shopping-cart", "remove_from_cart", key)
        setTimeout(() => {
            Unicorn.call("shopping-cart-counter", "update_cart_counter")
        }, 100)
    }

}
