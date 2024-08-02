export class Helpers {

    async customRequest(url, _method, _headers, _body = null) {
        return fetch(url, {
            method: _method,
            body: _body,
            headers: _headers
        })
        .then(response => response.json())
    }


    formatNumberAR(number) {
        return number.toLocaleString(
            "es-AR", 
            { 
                style: "decimal", 
                minimumFractionDigits: 2, 
                maximumFractionDigits: 2, 
                useGrouping: true 
            }
        )
    }

    
    openSideNavbar(buttons, element, classlist) {
        buttons.forEach(button => {
            button.addEventListener("click", () => {
                element.classList.toggle(classlist)
            })
        })
    }

}
