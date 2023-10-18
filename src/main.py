from fastapi import FastAPI, Response, APIRouter, Depends
from database.db import Database, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
# from fastapi.responses import RedirectResponse
from config import conf
from exchange import forms_router, exhange_router, menu_router
from sqladmin import Admin
from database.db import engine
from admin import (
    UserAdmin,
    ServicePaymentOptionAdmin,
    CurrencyAdmin, AdminAuth,
    PaymentOptionAdmin, ReviewAdmin,
    OrderAdmin,
)
from fastapi_users import FastAPIUsers
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.manager import get_user_manager
from database.models import User, Order
from binance_parser import find_price
import uuid


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_active_user = fastapi_users.current_user(active=True)

app = FastAPI(
    title="Exchange"
)
authentication_backend = AdminAuth(
    secret_key=conf.admin_auth
)

admin = Admin(
    app=app,
    engine=engine,
    authentication_backend=authentication_backend
)

admin.add_view(UserAdmin)
admin.add_view(ServicePaymentOptionAdmin)
admin.add_view(ReviewAdmin)
admin.add_view(CurrencyAdmin)
admin.add_view(PaymentOptionAdmin)
admin.add_view(OrderAdmin)


personal_account = APIRouter(
    prefix="/account",
    tags=["роутер личного кабинета"]
)


@app.get("/")
async def root(
    response: Response,
    async_session: AsyncSession = Depends(get_async_session),
):

    """Устанавливаем печеньки на пользователя"""
    cookies_uuid = uuid.uuid4()
    response.set_cookie(key="user_uuid", value=cookies_uuid)
    return cookies_uuid


@personal_account.get("/orders")
async def order_list(
    async_session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    db = Database(session=async_session)
    try:
        completed_orders = await db.order.get_many(
            Order.user_email == user.email
        )
        return completed_orders
    except KeyError("Ключ не найден"):
        return (" Нет совершенных сделок")


app.include_router(forms_router)
app.include_router(exhange_router)
app.include_router(menu_router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", log_level=conf.logging_level, reload=True)
