class CustomException(Exception):
    
    """ Custom exception for any bloody error. """

    def __init__(self, log: str, message: str, code: str = None, redirect: str = None) -> None:

        """
        CustomException Initializer.

        Args:
            log (str): Content to log.
            message (str): Message to display.
            code (str | None): Code name.
            redirect (str | None): Redirect site.
        """

        self.log = log
        self.message = message
        self.code = code
        self.redirect = redirect
        super().__init__(message, code, redirect)
        