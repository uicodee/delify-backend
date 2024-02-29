from fastapi import APIRouter

router = APIRouter(prefix="/order")


@router.get(
    path="/all"
)
async def get_all_orders():
    return {"ping": "pong"}
