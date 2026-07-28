# Token Service APIs

from fastapi import APIRouter, HTTPException

from app.services.token_service import token_service
from app.schemas.requests import ApproveRequest, MintRequest
from app.schemas.responses import TransactionResponse

router = APIRouter(prefix="/token", tags=["Token"])


@router.get("/total-supply")
def total_supply():
    return {"total_supply": token_service.total_supply()}


@router.get("/balance/{address}")
def get_balance(address: str):
    try:
        return {"address": address, "balance": token_service.balance_of(address)}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/mint", response_model=TransactionResponse)
def mint(request: MintRequest):
    return token_service.mint(request.address, request.amount)


@router.post("/approve", response_model=TransactionResponse)
def approve(request: ApproveRequest):
    return token_service.approve(request.amount)


@router.get("/allowance")
def allowance():
    return {"allowance": token_service.allowance()}
