from fastapi import APIRouter, Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from database.db import Database, get_async_session
from users.models import User


email_router = APIRouter(
    prefix="/api/email_verif",
    tags=["Роутер для верификации почты пользователя с лк"]
)


@email_router.post('/verif')
async def verify_email(
    verif_token: str,
    session: AsyncSession = Depends(get_async_session),
) -> bool | None:
    user = await Database(session).user.get_by_where(
        User.verification_token == verif_token
    )

    if user:
        await Database(session).user.update_verification(user.id)
        return True

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Пользователя нет в бд"
    )
