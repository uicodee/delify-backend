from fastapi import APIRouter

router = APIRouter(prefix="/product")

@router.get(
    path="/all"
)
async def get_all_products():
    return {"products": "all"}
