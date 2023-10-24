from auth.routers import current_active_verified_user 
from fastapi import FastAPI, Depends, APIRouter
from typing import TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_async_session, Database
from orders import Order
if TYPE_CHECKING:
    from users.models import User


orders_router = APIRouter(
    prefix="/account",
    tags=["роутер личного кабинета"]
)

@orders_router.get("/current_user/order_list")
async def order_list(
    async_session: AsyncSession = Depends(get_async_session),
    user: "User" = Depends(current_active_verified_user)
):
    db = Database(session=async_session)
    try:
        completed_orders = await db.order.get_many(
            Order.user_email == user.email
        )
        return completed_orders
    except KeyError("Ключ не найден"):
        return (" Нет совершенных сделок")