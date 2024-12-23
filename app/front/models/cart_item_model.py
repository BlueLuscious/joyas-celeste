from django.db import models
from back.models.client_model import ClientModel
from front.models.product_model import ProductModel


class CartItemModel(models.Model):

    """
    Cart Item Model.

    Fields:
        key (str): Mixing concatenation product uuid and product size.
        user (ClientModel): ClientModel Instance.
        product (ProductModel): Product Instance.
        price (Decimal): Cart item price.
        size (str): Product size.
        stock (int): Product stock.
        quantity (int): Cart item quantity
        created_at (DateTime): Creation date.
        updated_at (DateTime): Update date.
    """

    key = models.CharField(primary_key=True, max_length=128)
    user = models.ForeignKey(
        ClientModel, on_delete=models.DO_NOTHING, related_name="cart_item_user", default=None
    )
    product = models.ForeignKey(
        ProductModel, on_delete=models.DO_NOTHING, related_name="cart_item"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    size = models.CharField(max_length=128)
    stock = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Product name.
        """

        return self.product.name
