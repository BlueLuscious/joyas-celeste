import json


class JsonService:

    """ Service for json. """

    def is_loadable_json(self, data: str) -> bool:

        """
        Validate if a str is a loadable json.

        Args:
            data (str): Context.

        Returns:
            bool: If is a loadable json return `True` else `False`. 
        """

        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False
        