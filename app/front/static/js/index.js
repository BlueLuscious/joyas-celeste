document.addEventListener("DOMContentLoaded", () => {

    const categoryBox = Array.from(document.getElementsByClassName("category_box"))
    const categoryText = Array.from(document.getElementsByClassName("category_text"))
    const categoryLabel = Array.from(document.getElementsByClassName("category_label"))

    categoryBox.forEach((box, index) => {
        box.addEventListener("mouseover", () => {
            categoryText[index].style.display = "none"
            categoryLabel[index].classList.toggle("-translate-y-full")
        })
    })

    categoryBox.forEach((box, index) => {
        box.addEventListener("mouseout", () => {
            categoryText[index].style.display = "block"
            categoryLabel[index].classList.toggle("-translate-y-full")
        })
    })

})
