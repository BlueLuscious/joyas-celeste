import logging
from product.dtos.query_field_dto import QueryFieldDTO

logger = logging.getLogger(__name__)


class QueryFieldCollection:

    """ Collection of QueryFieldDTO's. """

    def __init__(self) -> None:

        """ QueryFieldCollection Initializer. """

        self.fields: dict[str, QueryFieldDTO] = {}


    def create_field(self, key: str, field_name: str, label: str) -> QueryFieldDTO:

        """
        Create a field in the collection.

        Args:
            key (str): QueryFieldDTO key.
            field_name (str): Field name.
            label (str): label.

        Returns:
            QueryFieldDTO: QueryFieldDTO Instance.
        """

        self.fields[key] = QueryFieldDTO(field_name, label)
        return self.fields[key]
    

    def get_field(self, key: str) -> QueryFieldDTO:

        """ 
        Get a field from the collection by key.

        Args:
            key (str): QueryFieldDTO key.

        Returns:
            QueryFieldDTO: QueryFieldDTO Instance.
        """

        return self.fields.get(key)
    

    def get_all_fields(self) -> dict[str, QueryFieldDTO]:

        """
        Get all fields from the collection.

        Returns:
            dict[str, QueryFieldDTO]: A collection of QueryFieldDTO's.
        """

        return self.fields
    