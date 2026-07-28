# Health APIs
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def get_status():
    return {"status": "ok"}
