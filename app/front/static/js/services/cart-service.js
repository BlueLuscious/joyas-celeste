import { Helpers } from "../helpers/helpers.js"
import { cartItemTemplate } from "../components/cart-item.js"

export class CartService {

    constructor() {
        this.helpers = new Helpers
        this.toolbox = new Toolbox
    }

    /**
     * Add Product To Cart Dynamically:
     * @param {Array.<HTMLElement>} buttons Buttons.
     * @returns {void} None.
     */
    addProduct(buttons) {
        buttons.forEach(button => {
            button.addEventListener("click", () => {
                
                const productUuid = button.getAttribute("data-id")
                const url = `/cart/${productUuid}/`
                const form = document.getElementById(`product_form_${productUuid}`)
                const formData = new FormData(form)
                const myHeaders = {
                    "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
                    "X-Requested-With": "XMLHttpRequest"
                }

                const response = this.helpers.customRequest(url, "POST", myHeaders, formData)
                response.then(data => {
                    console.log("Data: ", data)
                    const cartItemsContainer = document.getElementById("cart_items")

                    for (const [uuid, item] of Object.entries(data.cart.items)) {
                        let itemElement = document.querySelector(`[id^="item_${uuid}"]`)
                        
                        if (itemElement) {
                            itemElement.innerHTML = cartItemTemplate(uuid, item, "update")
                        } else {
                            const itemElement = document.createElement("div")
                            itemElement.id = `item_${uuid}`
                            itemElement.classList = "relative flex flex-col w-full"
                            itemElement.innerHTML = cartItemTemplate(uuid, item, "add")
                            cartItemsContainer.appendChild(itemElement)
                        }

                        const newSubtractButtons = document.querySelectorAll(`[id^="subtract_quantity_${uuid}"]`)
                        const newAddButtons = document.querySelectorAll(`[id^="add_quantity_${uuid}"]`)
                        this.updateQuantityProduct(newSubtractButtons, "subtract")
                        this.updateQuantityProduct(newAddButtons, "add")

                        const newRemoveButtons = document.querySelectorAll(`[id^="remove_${uuid}"]`)
                        this.removeProduct(newRemoveButtons)
                    }
                    
                    this.toolbox.updateBubbleCounter(data.cart.items)
                    
                })
                .catch(error => {
                    console.error("Error: ", error)
                })
            })
        })
    }


    /**
    * Remove Product To Cart Dynamically:
    * @param {Array.<HTMLElement>} buttons Buttons.
    * @returns {void} None.
    */
    removeProduct(buttons) {
        buttons.forEach(button => {
            button.addEventListener("click", () => {

                const productUuid = button.getAttribute("data-id")
                const url = `/cart/${productUuid}/`
                const myHeaders = {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                    "X-Requested-With": "XMLHttpRequest"
                }

                const response = this.helpers.customRequest(url, "DELETE", myHeaders)
                response.then(data => {
                    console.log("Data: ", data)
                    const itemElement = document.getElementById(`item_${productUuid}`)

                    if (itemElement) {
                        itemElement.remove()

                        this.toolbox.updateBubbleCounter(data.cart.items)
                    }

                }).catch(error => {
                    console.error("Error:", error)
                })
            })
        })
    }


    /**
    * Update Quantity Product To Card Dynamically:
    * @param {Array.<HTMLElement>} buttons Buttons.
    * @param {string} action Action to perform (add or subtract).
    * @returns {void} None.
    */
    updateQuantityProduct(buttons, action) {
        buttons.forEach(button => {
            button.addEventListener("click", () => {
    
                const productUuid = button.getAttribute("data-id")
                const url = `/cart/${action}/${productUuid}/`
                const myHeaders = {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                    "X-Requested-With": "XMLHttpRequest"
                }

                const response = this.helpers.customRequest(url, "POST", myHeaders)
                response.then(data => {
                    console.log("Data: ", data)
                    
                    for (const [uuid, item] of Object.entries(data.cart.items)) {
                        let itemElement = document.querySelector(`[id^="item_${uuid}"]`)
                        
                        if (itemElement) {
                            itemElement.innerHTML = cartItemTemplate(uuid, item, "update")
                        }

                        const newSubtractButtons = document.querySelectorAll(`[id^="subtract_quantity_${uuid}"]`)
                        const newAddButtons = document.querySelectorAll(`[id^="add_quantity_${uuid}"]`)
                        this.updateQuantityProduct(newSubtractButtons, "subtract")
                        this.updateQuantityProduct(newAddButtons, "add")

                        const newRemoveButtons = document.querySelectorAll(`[id^="remove_${uuid}"]`)
                        this.removeProduct(newRemoveButtons)
                    }

                }).catch(error => {
                    console.error("Error:", error)
                })
            })
        })
    }


}


class Toolbox {

    /**
    * Update Bubble Counter Dynamically:
    * @param {json} items Product Data.
    * @returns {void} None.
    */
    updateBubbleCounter(items) {
        const bubbleCounter = document.getElementById("bubble_counter")
        const itemCount = Object.keys(items).length
        bubbleCounter.textContent = itemCount
    }

}
