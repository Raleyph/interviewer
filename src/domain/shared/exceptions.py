class DomainException(Exception):
    error_code: str = "DOMAIN_ERROR"
    message: str = "Internal business error"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.message)

    def to_dict(self) -> dict:
        return {
            "error_code": self.error_code,
            "message": self.message
        }


class InvalidEmailException(DomainException):
    pass
