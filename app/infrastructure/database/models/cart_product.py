from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class CartProduct(BaseModel):

    __tablename__ = "cart_product"

    cart_id: Mapped[int] = mapped_column(ForeignKey("cart.id", ondelete="CASCADE"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id", ondelete="CASCADE"))
    