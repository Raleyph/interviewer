from uuid import UUID

from src.domain.shared.entity import Entity
from src.domain.shared.value_objects import Email
from src.domain.user.value_objects import ExternalIdentity


class User(Entity):
    def __init__(
            self,
            identity: ExternalIdentity,
            email: Email | None,
            username: str | None,
            is_active: bool = True,
            id_: UUID | None = None
    ):
        self._identity = identity
        self._email = email
        self._username = username
        self._is_active = is_active
        super().__init__(id_=id_)

    # props

    @property
    def identity(self) -> ExternalIdentity:
        return self._identity

    @property
    def email(self) -> Email | None:
        return self._email

    @property
    def username(self) -> str | None:
        return self._username

    @property
    def is_active(self) -> bool:
        return self._is_active

    # factory

    @staticmethod
    def create():
        pass

    # business logic

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False
