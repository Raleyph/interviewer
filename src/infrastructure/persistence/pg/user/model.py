from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.pg.shared import Base


class UserORM(Base):
    __tablename__ = "users"

    auth_provider: Mapped[str] = mapped_column(nullable=False)
    auth_subject: Mapped[str] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column()

    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)
    last_login_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
