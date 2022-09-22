class ProductIsInvalidKeyException(KeyError):
    def __init__(self, key: str):
        self.key = key

    def __str__(self):
        return f"{self.key} should be valid."
