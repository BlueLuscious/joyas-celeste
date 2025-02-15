export class ProductService {

    /**
    * Search products by text:
    * 
    * Use Unicorn to call methods, get products by text.
    * @returns {void} None.
    */
    static setSearchText() {
        Unicorn.call("products", "update_products")
    }

}
