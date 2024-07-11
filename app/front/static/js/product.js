document.addEventListener("DOMContentLoaded", function() {
    const imageContainer = document.getElementById("image_container")
    const zoomImage = document.getElementById("zoom_image")

    imageContainer.addEventListener("mousemove", event => {
        const rect = imageContainer.getBoundingClientRect()
        const x = event.clientX - rect.left
        const y = event.clientY - rect.top

        const xPercent = x / rect.width * 100
        const yPercent = y / rect.height * 100

        zoomImage.style.transformOrigin = `${xPercent}% ${yPercent}%`
        zoomImage.style.transform = "scale(2)"
    })

    imageContainer.addEventListener("mouseleave", () => {
        zoomImage.style.transformOrigin = "center center"
        zoomImage.style.transform = "scale(1)"
    })
})
