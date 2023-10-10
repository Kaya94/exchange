from .base import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from .crypto_type import CryptoType


class Currency(Base):
    __tablename__ = "currency"

    id: Mapped[int] = mapped_column(
        sa.BigInteger,
        primary_key=True,
        autoincrement=True
    )
    tikker: Mapped[str] = mapped_column(
        sa.Text,
        unique=True,
        nullable=False,
    )
    type: Mapped[CryptoType] = mapped_column(
        sa.Enum(CryptoType)
    )
    name: Mapped[str] = mapped_column(
        sa.Text,
        unique=True,
        nullable=False
    )
    gas: Mapped[sa.Numeric] = mapped_column(
        sa.Numeric,
        default=130,
        nullable=False
    )
    service_margin: Mapped[sa.Numeric] = mapped_column(
        sa.Numeric,
        default=7,
        nullable=False
    )
    reserve: Mapped[sa.Numeric] = mapped_column(
        sa.Numeric,
        default=0,
    )
    max: Mapped[sa.Numeric] = mapped_column(
        sa.Numeric,
        default=0,
    )
    min: Mapped[sa.Numeric] = mapped_column(
        sa.Numeric,
        default=0,
    )
    icon: Mapped[str] = mapped_column(
        sa.Text,
        default=None,
        nullable=True
    )
