from fastapi import FastAPI
from .authentication import router as authentication_router
from .cart import router as cart_router
from .cart_product import router as cart_product_router
from .category import router as category_router
from .courier import router as courier_router
from .order import router as order_router
from .product import router as product_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=authentication_router,
        tags=["Authentication"]
    )
    app.include_router(
        router=cart_router,
        tags=["Cart"]
    )
    app.include_router(
        router=cart_product_router,
        tags=["CartProduct"]
    )
    app.include_router(
        router=category_router,
        tags=["Category"]
    )
    app.include_router(
        router=courier_router,
        tags=["Courier"]
    )
    app.include_router(
        router=order_router,
        tags=["Order"]
    )
    app.include_router(
        router=product_router,
        tags=["Product"]
    )
