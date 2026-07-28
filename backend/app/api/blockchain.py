# Blockchain APIs
from fastapi import APIRouter

from app.blockchain.client import blockchain_client

router = APIRouter(prefix="/blockchain", tags=["Blockchain"])


@router.get("/status")
def get_status():
    return {"connected": blockchain_client.is_connected()}
