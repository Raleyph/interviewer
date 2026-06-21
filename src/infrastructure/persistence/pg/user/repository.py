from src.domain.user import IUserRepository
from src.infrastructure.persistence.pg.shared import PostgreSqlRepository


class UserRepository(PostgreSqlRepository, IUserRepository):
    pass
