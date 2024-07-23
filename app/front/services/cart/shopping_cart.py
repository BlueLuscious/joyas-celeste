from front.models.product_model import ProductModel

class ShoppingCart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

        self.stock = request.POST.get("product_stock")
        self.title = request.POST.get("product_name")
        self.price = request.POST.get("product_price")
        self.size = request.POST.get("product_size")
        self.quantity = 0


    def json(self):
        return {
            "stock": self.stock,
            "name": self.title,
            "price": self.price,
            "size": self.size,
            "quantity": self.quantity,
        }


    def add_to_cart(self, product, quantity=1):
        product_uuid = str(product.uuid)
        if product_uuid not in self.cart:
            self.cart[product_uuid] = self.json()
        self.cart[product_uuid]['quantity'] += quantity
        self.save_cart()
        # self.clean_cart()


    def remove_from_cart(self, product):
        product_uuid = str(product.uuid)
        if product_uuid in self.cart:
            del self.cart[product_uuid]
            self.save_cart()


    # def update_cart(self, product, quantity):
    #     product_uuid = str(product.uuid)
    #     if product_uuid in self.cart:
    #         self.cart[product_uuid]['quantity'] = quantity
    #         self.save_cart()


    def clean_cart(self):
        self.session['cart'] = {}
        # del self.session['cart']
        self.save_cart()


    def save_cart(self):
        self.session.modified = True


    def total(self):
        return sum(int(item['quantity']) * float(item['price']) for item in self.cart.values())
