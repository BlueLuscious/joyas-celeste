export class CartService {

    constructor() {
        
    }


    
    addProduct(buttons) {
        buttons.forEach(button => {
            button.addEventListener('click', event => {
                event.preventDefault()
                
                const productId = button.getAttribute('data-id')
                const form = document.getElementById(`product_form_${productId}`)
                const formData = new FormData(form)
                formData.append('quantity', 1)
    
                fetch(`/cart/add/${productId}/`, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        throw new Error('Network response was not ok.')
                    }
                })
                .then(data => {
                    console.log(data)
                    const cartItemsContainer = document.getElementById('cart_items')

                    for (const [productId, productDetails] of Object.entries(data.cart.items)) {
                        let itemElement = document.querySelector(`[id^="data_${productId}"]`)
                        
                        if (itemElement) {
                            itemElement.innerHTML = `Cantidad: ${productDetails.quantity}`
                        } else {
                            const itemElement = document.createElement('div')
                            itemElement.id = `item_${productId}`
                            itemElement.innerHTML = `
                                <div id="data_${productId}">Cantidad: ${productDetails.quantity}</div>
                                <div>Precio: ${productDetails.price}</div>
                                <button class="delete_item" data-id="${productId}">Eliminar</button>
                            `
                            cartItemsContainer.appendChild(itemElement)
                            const newDeleteButtons = document.querySelectorAll('.delete_item')
                            this.removeProduct(newDeleteButtons)
                        }
                        
                    }
                    
                })
                .catch(error => {
                    console.error('Error:', error)
                    alert("Hubo un error al procesar la solicitud.")
                })
            })
        })
    }


    removeProduct(buttons) {
        buttons.forEach(button => {
            button.addEventListener('click', event => {
                event.preventDefault()
    
                const productId = button.getAttribute('data-id')
    
                fetch(`/cart/remove/${productId}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        throw new Error('Network response was not ok.')
                    }
                })
                .then(data => {
                    console.log(data)
                    const itemElement = document.getElementById(`item_${productId}`)
                    if (itemElement) {
                        itemElement.remove()
                    }
                    // Actualiza el total del carrito si es necesario
                })
                .catch(error => {
                    console.error('Error:', error)
                    alert("Hubo un error al procesar la solicitud.")
                })
            })
        })
    }


}
