from django.contrib import messages
from django_unicorn.components import UnicornView
from front.models.cart_item_model import CartItemModel
from front.models.product_model import ProductModel


class ShoppingCartView(UnicornView):
    cart_items: CartItemModel

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.update_cart_items()


    def create_item(self, product: ProductModel, size: int, quantity: int) -> None:
        CartItemModel.objects.create(
            key = f"{str(product.uuid)}_{size}",
            product = product,
            price = product.price,
            size = size,
            stock = product.variations.filter(measure__size=size).first().stock,
            quantity = quantity
        )


    def add_to_cart(self, product: ProductModel, size: int, quantity: int = 1) -> None:
        key = f"{str(product.uuid)}_{size}"
        if not CartItemModel.objects.filter(key=key).exists():
            self.create_item(product, size, quantity)
            messages.success(self.request, "Producto agregado al carrito exitosamente")
        else:
            self.increment_quantity(product, key)
            messages.success(self.request, "Producto actualizado del carrito exitosamente")
        self.update_cart_items()


    def remove_from_cart(self, key: str) -> None:
        CartItemModel.objects.get(key=key).delete()
        messages.success(self.request, "Producto removido del carrito exitosamente")
        self.update_cart_items()


    def increment_quantity(self, product: ProductModel, key: str, quantity: int = 1) -> None:
        cart_item = CartItemModel.objects.get(key=key)
        if cart_item.quantity < cart_item.stock:
            cart_item.quantity += quantity
            cart_item.price = product.price * cart_item.quantity
        cart_item.save()
        self.update_cart_items()
        

    def decrement_quantity(self, product: ProductModel, key: str, quantity: int = 1) -> None:
        cart_item = CartItemModel.objects.get(key=key)
        if cart_item.quantity > 1:
            cart_item.quantity -= quantity
            cart_item.price = product.price * cart_item.quantity
        cart_item.save()
        self.update_cart_items()
        

    def clean_cart(self) -> None:
        CartItemModel.objects.all().delete()
        self.update_cart_items()


    def update_cart_items(self) -> None:
        self.cart_items = CartItemModel.objects.all()


    # def total(self, product: ProductModel) -> None:
    #     return sum(float(product.price) * item["quantity"] for item in self.cart.values())
