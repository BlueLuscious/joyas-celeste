import logging
from django.core.cache import cache
from django.db.models.query_utils import DeferredAttribute
from django.http import HttpRequest
from back.services.cripto_ya_service import CriptoYaService
from product.models.category_model import CategoryModel
from product.models.product_model import ProductModel
from product.models.subcategory_model import SubcategoryModel
from product.services.query_field_service import QueryFieldService

logger = logging.getLogger(__name__)


def common_context(request: HttpRequest) -> dict:

    categories = cache.get("categories")
    if not categories:
        categories = CategoryModel.objects.all()
        cache.set("categories", categories, timeout=3600)
    
    subcategories = cache.get("subcategories")
    if not subcategories:
        subcategories = SubcategoryModel.objects.all()
        cache.set("subcategories", subcategories, timeout=3600)

    dollar_blue_ask: float | None = cache.get("dollar_blue_ask")
    if not dollar_blue_ask:
        cripto_ya_service = CriptoYaService()
        dollar_quotes: dict[dict, dict] = cripto_ya_service.get_dollar_quotes()
        dollar_blue_ask: float = dollar_quotes.get("blue").get("ask")
        cache.set("dollar_blue_ask", dollar_blue_ask, timeout=3600)

    context = dict(
        categories=categories,
        subcategories=subcategories,
        dollar_blue=dollar_blue_ask,
    )

    logger.info(f"Common context: {context}")
    return context


def filters_and_orders_context(request: HttpRequest) -> dict:

    query_field_service = QueryFieldService()

    name_field: DeferredAttribute = ProductModel.name
    query_field_service.create_query_field_lookups(name_field.field.name, "A a Z")
    name_orders = query_field_service.get_query_field_lookups(name_field.field.name)

    price_field: DeferredAttribute = ProductModel.price
    query_field_service.create_query_field_lookups(price_field.field.name, "Menor a Mayor")
    price_orders = query_field_service.get_query_field_lookups(price_field.field.name)

    created_at_field: DeferredAttribute = ProductModel.created_at
    query_field_service.create_query_field_lookups(created_at_field.field.name, "Antiguo a Nuevo")
    created_at_orders = query_field_service.get_query_field_lookups(created_at_field.field.name)

    context = dict(
        name_orders=name_orders,
        price_orders=price_orders,
        created_at_orders=created_at_orders,
    )

    logger.info(f"Filters and orders context: {context}")
    return context
