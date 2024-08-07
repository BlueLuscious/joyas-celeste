import { Helpers } from "../helpers/helpers.js"
const helpers = new Helpers


/**
 * Get Cart Item Template:
 * @param {string} uuid Product UUID.
 * @param {json} item Product data.
 * @param {string} action Action to perform (add or update).
 * @returns {string} HTML Template.
 */
export function cartItemTemplate(uuid, item, action) {

    if (action == "update") {
        item.price = item.base_price * item.quantity
    }

    const template = `
        <div class="flex flex-row w-full">
            <div class="w-2/5">
                <img class="w-full rounded-tl-sm" src="${ item.image }" alt="image">
            </div>
            <div class="flex flex-col items-center justify-center gap-y-2 w-3/5">
                <div>${ item.name }</div>
                <div class="font-semibold">$ ${ helpers.formatNumberAR(item.price) }</div>
                <div>Talle ${ item.size }</div>
            </div>
        </div>
        <div class="flex flex-row items-center justify-around p-2.5 bg-primary-earth_tone_3_light">
            <button id="subtract_quantity_${ uuid }" data-id="${ uuid }"
                class="p-2 px-3 text-white bg-primary-earth_tone_4 rounded-sm">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" 
                    stroke-width="1.75" stroke="currentColor" class="size-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14" />
                </svg>
            </button>
            <div id="quantity_${ uuid }" 
                class="w-1/4 p-0.5 text-center text-primary-earth_tone_4 bg-white border-2
                border-primary-earth_tone_4 rounded-md">
                ${ item.quantity }
            </div>
            <button id="add_quantity_${ uuid }" data-id="${ uuid }"
                class="p-2 px-3 text-white bg-primary-earth_tone_4 rounded-sm">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" 
                    stroke-width="1.75" stroke="currentColor" class="size-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                </svg>
            </button>
        </div>
        <button id="remove_${ uuid }" class="absolute top-1 right-1" data-id="${ uuid }">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" 
                stroke-width="1.5" stroke="currentColor" class="size-6 text-red-700">
                <path stroke-linecap="round" stroke-linejoin="round" 
                d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
            </svg>  
        </button>
    `

    return template

}
