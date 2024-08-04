from django.http import HttpRequest
from front.models.product_model import ProductModel


class ShoppingCart:

    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        self.cart = self.session.get("cart")
        if not self.cart:
            self.cart = self.session["cart"] = {}
        self.price = request.POST.get("product_price")
        self.size = request.POST.get("product_size")


    def create_item(self, product: ProductModel, quantity: int) -> dict:
        return {
            "uuid": str(product.uuid),
            "name": product.name,
            "price": float(self.price),
            "base_price": float(self.price),
            "size": self.size,
            "stock": product.stock,
            "image": product.image.url,
            "quantity": quantity,
        }


    def add_to_cart(self, product: ProductModel, quantity: int = 1) -> None:
        key = f"{str(product.uuid)}_{self.size}"
        if key not in self.cart:
            self.cart[key] = self.create_item(product, quantity)
        else:
            self.increment_quantity(str(product.uuid), self.size)
        self.save_cart()


    def remove_from_cart(self, uuid: str, size: str) -> None:
        key = f"{str(uuid)}_{size}"
        if key in self.cart:
            del self.cart[key]
        self.save_cart()


    def increment_quantity(self, uuid: str, size: str, quantity: int = 1) -> None:
        key = f"{str(uuid)}_{size}"
        if self.cart[key]["quantity"] < self.cart[key]["stock"]:
            self.cart[key]["quantity"] += quantity
            self.cart[key]["price"] = self.cart[key]["base_price"] * self.cart[key]["quantity"]


    def decrement_quantity(self, uuid: str, size: str, quantity: int = 1) -> None:
        key = f"{str(uuid)}_{size}"
        if self.cart[key]["quantity"] > 1:
            self.cart[key]["quantity"] -= quantity
            self.cart[key]["price"] = self.cart[key]["base_price"] * self.cart[key]["quantity"]


    def clean_cart(self) -> None:
        self.session["cart"] = {}
        self.save_cart()


    def save_cart(self) -> None:
        self.session.modified = True


    def total(self) -> None:
        return sum(item["quantity"] * item["base_price"] for item in self.cart.values())
