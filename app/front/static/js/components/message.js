/**
 * Get Message Template:
 * @param {string} message Message.
 * @param {string} type Message type.
 * @returns {string} HTML Template.
 */
export function messageTemplate(message, type) {
    const template = `
        <div class="flex flex-row items-center justify-between w-full sm:w-1/2 lg:w-1/3 p-4 bg-green-50 
            text-md md:text-lg text-green-600 text-center border-l-2 border-green-600 rounded-md">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" 
                    stroke-width="1.75" stroke="currentColor" class="size-5 md:size-6">
                    <path stroke-linecap="round" stroke-linejoin="round" 
                        d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                </svg>              
            </div>
            <div class="flex items-center justify-center w-full">
                <div id="message_content" class="font-medium mukta-light">
                    ${message}
                </div>
            </div>
        </div>
    `

    return template
}
