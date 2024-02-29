from fastapi import APIRouter

router = APIRouter(prefix="/cart-product")


@router.get(
    path="/all"
)
async def get_all_cart_products():
    return {"message": "All cart products"}
