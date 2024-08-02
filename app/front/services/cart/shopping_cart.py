from django.http import HttpRequest
from front.models.product_model import ProductModel


class ShoppingCart:

    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        self.cart = self.session.get("cart", {})
        self.price = request.POST.get("product_price")
        self.size = request.POST.get("product_size")


    def create_item(self, product: ProductModel, quantity: int) -> dict:
        return {
            "name": product.name,
            "price": float(self.price),
            "base_price": float(self.price),
            "size": self.size,
            "stock": product.stock,
            "image": product.image.url,
            "quantity": quantity,
        }


    def add_to_cart(self, product: ProductModel, quantity: int = 1) -> None:
        product_uuid = str(product.uuid)
        if product_uuid not in self.cart:
            self.cart[product_uuid] = self.create_item(product, quantity)
        else:
            self.increment_quantity(product_uuid, quantity)
        self.save_cart()


    def remove_from_cart(self, product: ProductModel) -> None:
        product_uuid = str(product.uuid)
        if product_uuid in self.cart:
            del self.cart[product_uuid]
        self.save_cart()


    def increment_quantity(self, uuid: str, quantity: int) -> None:
        if self.cart[uuid]["quantity"] < self.cart[uuid]["stock"]:
            self.cart[uuid]["quantity"] += quantity
            self.cart[uuid]["price"] = self.cart[uuid]["base_price"] * self.cart[uuid]["quantity"]


    def decrement_quantity(self, uuid: str, quantity: int) -> None:
        if self.cart[uuid]["quantity"] > 1:
            self.cart[uuid]["quantity"] -= quantity
            self.cart[uuid]["price"] = self.cart[uuid]["base_price"] * self.cart[uuid]["quantity"]


    def clean_cart(self) -> None:
        self.session["cart"] = {}
        self.save_cart()


    def save_cart(self) -> None:
        self.session.modified = True


    def total(self) -> None:
        return sum(item["quantity"] * item["base_price"] for item in self.cart.values())
