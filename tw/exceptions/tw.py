"""exception module"""

class TwError(Exception):
    """
        Just a custom exception, overriding Exception needed methods
    """
    
    def __init__(self, message: str):
        super().__init__(message)
        
        self.message = message
        
    def __str__(self) -> str:
        return self.message
