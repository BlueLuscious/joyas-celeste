import logging
from product.collections.query_field_collection import QueryFieldCollection
from product.dtos.query_field_dto import QueryFieldDTO

logger = logging.getLogger(__name__)


class QueryFieldService:

    """ Service for QueryFieldDTO. """

    def __init__(self) -> None:

        """ QueryFieldService Initializer. """

        self.query_field_collection = QueryFieldCollection()


    def create_query_field_lookups(self, field_name: str, label: str) -> QueryFieldCollection:

        """
        Create a list of QueryFieldDTO by a field name.

        Args:
            field_name (str): Field name.
            label (str): Label.

        Returns:
            QueryFieldCollection: QueryFieldCollection Object.
        """

        self.query_field_collection.create_field(
            f"asc_{field_name}", field_name, label
        )

        split_label: list[str] = label.split(" a ")
        reversed_label: str = f"{split_label[1].capitalize()} a {split_label[0].capitalize()}"
        self.query_field_collection.create_field(
            f"desc_{field_name}", f"-{field_name}", reversed_label
        )

        return self.query_field_collection


    def get_query_field_lookups(self, field_name: str) -> list[QueryFieldDTO]:

        """
        Get a list of QueryFieldDTO by a field name.

        Args:
            field_name (str): Field name.
            label (str): Label.

        Returns:
            list[QueryFieldDTO]: A list of QueryFieldDTO Instances.
        """

        query_fields: list = [
            self.query_field_collection.get_field(f"asc_{field_name}"),
            self.query_field_collection.get_field(f"desc_{field_name}")
        ]

        return query_fields
    