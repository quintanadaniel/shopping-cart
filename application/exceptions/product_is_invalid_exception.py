class ProductIsInvalidException(Exception):
    """Class to define when Product is invalid and return an exception"""
    def __init__(self, key: str):
        self.key = key

    def __str__(self):
        return f"{self.key} should be valid."
