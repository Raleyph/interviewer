from datetime import datetime

from sqlalchemy import DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.pg.shared import Base


class UserORM(Base):
    __tablename__ = "users"

    auth_provider: Mapped[str] = mapped_column(nullable=False)
    auth_subject: Mapped[str] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    display_name: Mapped[str | None] = mapped_column(nullable=True)

    is_active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
        server_default="true"
    )

    last_login_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    __table_args__ = (
        UniqueConstraint(
            "auth_provider",
            "auth_subject",
            name="uq_users_auth_provider_subject"
        ),
        UniqueConstraint("email", name="nq_users_email"),
        UniqueConstraint("username", name="nq_users_username")
    )
