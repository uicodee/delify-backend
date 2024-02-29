from sqlalchemy import ForeignKey, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.dto import OrderStatus
from app.infrastructure.database.models import BaseModel


class Order(BaseModel):

    __tablename__ = "order"

    cart_id: Mapped[int] = mapped_column(ForeignKey("cart.id", ondelete="NO ACTION"))
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus))
    total_price: Mapped[float] = mapped_column(Float)
    delivery_price: Mapped[float] = mapped_column(Float)
