class MyCustomError(TypeError):
    """
    Exception raised when a specific error is needed
    """
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code

raise MyCustomError("We have a error in code", 500)