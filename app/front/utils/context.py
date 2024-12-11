class Context:

    """ Data entity that represents a context based on the data provided. """

    def __init__(self, *args, **kwargs) -> None:

        """
        Context Initializer.

        Args:
           *args (tuple): Positional arguments to define the context.
           **kwargs (dict): Keyword arguments to define the context.
        """

        super().__init__()
        self.args = args
        self.kwargs = kwargs

    @property
    def as_dict(self) -> dict:

        """
        A dictionary with Context data 

        Returns:
            dict: A dictionary based on the data provided.
        """

        return { **self.kwargs }
    