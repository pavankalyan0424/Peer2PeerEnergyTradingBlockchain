# Health APIs
from fastapi import APIRouter

router = APIRouter(prefix="/health")


@router.get("")
def get_status():
    return {"status": "ok"}
