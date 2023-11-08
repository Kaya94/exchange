"""  Order repository file """
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from orders.models import Order
from currencies.models import Currency
from payment_options.models import PaymentOption
from enums import Status
from users.models import User
from service_payment_options.models import ServicePaymentOption
from database.abstract_repo import Repository
from sqlalchemy import update


class OrderRepo(Repository[Order]):
    """
    Order repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize Order repository as for all Orders
        or only for one
        """
        super().__init__(type_model=Order, session=session)

    async def new(
        self,
        user_id: User,
        user_email: User,
        user_cookie: str,
        user_buy_sum: sa.Numeric,
        sell_currency_id: Currency,
        buy_payment_option_id: PaymentOption,
        user_sell_sum: sa.Numeric,
        buy_currency_id: Currency,
        sell_payment_option_id: PaymentOption,
        status: Status,
        service_sell_po_id: ServicePaymentOption = None,
        service_buy_po_id: ServicePaymentOption = None,
    ) -> None:

        new_order = await self.session.merge(
            Order(
                user_id=user_id,
                user_email=user_email,
                user_cookie=user_cookie,
                user_buy_sum=user_buy_sum,
                buy_currency_id=buy_currency_id,
                buy_payment_option_id=buy_payment_option_id,
                user_sell_sum=user_sell_sum,
                sell_currency_id=sell_currency_id,
                sell_payment_option_id=sell_payment_option_id,
                status=status,
                service_sell_po_id=service_sell_po_id,
                service_buy_po_id=service_buy_po_id,
            )
        )
        return new_order

    async def order_status_timout(
            self,
            order_id: int
    ) -> None:
        statement = (
            update(Order).
            where(Order.id == order_id).
            values(status=Status.Timeout)
        )
        return (await self.session.execute(statement)).scalar_one_or_none()
    