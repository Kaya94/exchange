"""  User repository file """
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import (
    User,
)
from .abstract import Repository


class UserRepo(Repository[User]):
    """
    User repository for CRUD
    and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize User
        repository as for all User
        or only for one
        """
        super().__init__(type_model=User, session=session)

    async def new(
        self,
        email: str,
        first_name: str,
        second_name: str,
    ) -> None:

        new_user = await self.session.merge(
            User(
                email=email,
                first_name=first_name,
                second_name=second_name,
            )
        )
        return new_user
