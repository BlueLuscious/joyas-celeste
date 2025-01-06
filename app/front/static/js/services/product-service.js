export class ProductService {

    /**
    * Search products by text:
    * 
    * Use Unicorn to call methods, get products by text.
    * @returns {void} None.
    */
    static setSearchText() {
        const search = document.getElementById("search_text").value.trim()
        Unicorn.call("products", "set_selected_query", "selected_search_text", search)
    }

}
