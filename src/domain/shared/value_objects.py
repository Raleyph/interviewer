from dataclasses import dataclass

from email_validator import validate_email, EmailNotValidError

from src.domain.shared.exceptions import InvalidEmailException


@dataclass(frozen=True)
class ValueObject:
    pass


@dataclass(frozen=True)
class Email(ValueObject):
    value: str

    def __post_init__(self):
        try:
            normalized = validate_email(self.value, check_deliverability=True).normalized
            object.__setattr__(self, "value", normalized)
        except EmailNotValidError as exc:
            raise InvalidEmailException() from exc

    def __str__(self) -> str:
        return self.value
