import logging
from django.core.cache import cache
from django.http import HttpRequest
from back.services.cripto_ya_service import CriptoYaService
from back.utils.models.query_field_service import QueryFieldService
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.models.subcategory_model import SubcategoryModel

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

    name_field = ProductModel.name.field.name
    query_field_service.create_query_field_lookups(name_field, "A a Z")
    name_orders = query_field_service.get_query_field_lookups(name_field)

    price_field = ProductModel.price.field.name
    query_field_service.create_query_field_lookups(price_field, "Menor a Mayor")
    price_orders = query_field_service.get_query_field_lookups(price_field)

    created_at_field = ProductModel.created_at.field.name
    query_field_service.create_query_field_lookups(created_at_field, "Antiguo a Nuevo")
    created_at_orders = query_field_service.get_query_field_lookups(created_at_field)

    context = dict(
        name_orders=name_orders,
        price_orders=price_orders,
        created_at_orders=created_at_orders,
    )

    logger.info(f"Filters and orders context: {context}")
    return context
