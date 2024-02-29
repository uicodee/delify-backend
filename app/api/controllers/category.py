from fastapi import APIRouter

router = APIRouter(prefix="/category")


@router.get(
    path="/all"
)
async def get_categories():
    return {"categories": "all"}