from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class Courier(BaseModel):

    __tablename__ = "courier"

    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    orders: Mapped[int] = mapped_column(Integer, default=0)
    rating: Mapped[float] = mapped_column(Float, default=5)
    active_order_id: Mapped[int] = mapped_column(ForeignKey("order.id", ondelete="NO ACTION"))
