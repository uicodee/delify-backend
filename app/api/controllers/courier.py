from fastapi import APIRouter

router = APIRouter(prefix="/courier")


@router.get(
    path="/all"
)
async def get_all_couriers():
    return {"ping": "pong"}

