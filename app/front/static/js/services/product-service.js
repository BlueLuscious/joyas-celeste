export class ProductService {

    /**
    * Search products by text:
    * 
    * Use Unicorn to call methods, get products by text.
    * @returns {void} None.
    */
    static setSearchText() {
        const search = document.getElementById("search_text").value.trim()
        Unicorn.call("products", "set_selected_queries", "selected_search_text", search)
    }

    /**
    * Set selected queries (Filters, orders, etc.).
    * 
    * Use Unicorn to call methods, send form data to set queries.
    * @returns {void} None.
    */
    static setSelectedQueries() {
        let form = document.getElementById("queries_form")
        let formData = new FormData(form)

        let keyList = []
        let valueList = []
        formData.forEach((value, key) => {
            keyList.push(key.trim())
            valueList.push(value.trim())
        })

        Unicorn.call("products", "set_selected_queries", JSON.stringify(keyList), JSON.stringify(valueList))
    }

}
