from dataclasses import dataclass


@dataclass
class QueryFieldDTO:

    """
    DTO for Fields to filter, order, etc. 

    Properties:
        uuid (str): Field name.
        name (str): Label.
    """

    uuid: str
    name: str
    