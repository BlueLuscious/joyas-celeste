class CustomException(Exception):
    
    """ Custom exception for any bloody error. """

    def __init__(self, message: str, code: str = None, redirect: str = None) -> None:
        self.message = message
        self.code = code
        self.redirect = redirect
        super().__init__(message, code, redirect)
        