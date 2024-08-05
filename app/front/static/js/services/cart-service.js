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
                const url = `/cart/add/${productUuid}/`
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

                            if (!item.no_stock) {
                                const message = "Producto actualizado exitosamente"
                                this.toolbox.displayNotificationMessage(message)
                            }
                        } else {
                            const itemElement = document.createElement("div")
                            itemElement.id = `item_${uuid}`
                            itemElement.classList = "relative flex flex-col w-full"
                            itemElement.innerHTML = cartItemTemplate(uuid, item, "add")
                            cartItemsContainer.appendChild(itemElement)

                            const message = "Producto agregado exitosamente"
                            this.toolbox.displayNotificationMessage(message)
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
                const url = `/cart/remove/${productUuid}/`
                const myHeaders = {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                    "X-Requested-With": "XMLHttpRequest"
                }

                const response = this.helpers.customRequest(url, "POST", myHeaders)
                response.then(data => {
                    console.log("Data: ", data)
                    const itemElement = document.getElementById(`item_${productUuid}`)

                    if (itemElement) {
                        itemElement.remove()

                        const message = "Producto removido exitosamente"
                        this.toolbox.displayNotificationMessage(message)

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
                const url = `/cart-item/${action}/${productUuid}/`
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


    /**
    * Display Notification:
    * @param {string} message Message.
    * @returns {void} None.
    */
    displayNotificationMessage(message) {
        const messageContainer = document.getElementById("message_container")

        const msg = document.createElement("div")
        msg.id = "message"
        msg.classList = "z-10 fixed top-24 flex justify-end w-full p-4 transform translate-x-full transition-transform duration-300 ease-in-out"
        msg.innerHTML = `
            <div class="flex flex-row items-center justify-between w-full sm:w-1/2 lg:w-1/3 p-4 bg-green-50 
                text-md md:text-lg text-green-600 text-center border-l-2 border-green-600 rounded-md">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" 
                        stroke-width="1.5" stroke="currentColor" class="size-5 md:size-6">
                        <path stroke-linecap="round" stroke-linejoin="round" 
                            d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>              
                </div>
                <div class="flex items-center justify-center w-full">
                    <div id="message_content" class="mukta-light">
                        ${message}
                    </div>
                </div>
            </div>
        `
        messageContainer.appendChild(msg)

        setTimeout(() => {
            msg.classList.toggle("translate-x-full")
            setTimeout(() => {
                msg.classList.toggle("translate-x-full")
                setTimeout(() => {
                    msg.remove()
                }, 2300)
            }, 2200)
        }, 300)

    }

}
