from dataclasses import dataclass

from src.domain.shared.value_objects import ValueObject


@dataclass(frozen=True)
class ExternalIdentity(ValueObject):
    provider: str
    subject: str
