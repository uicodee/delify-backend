from fastapi import APIRouter

router = APIRouter(prefix="/cart")


@router.get(
    path="/all"
)
async def get_all():
    return {"ping": "pong"}
