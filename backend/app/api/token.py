# Token Service APIs

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.blockchain.token import token_service

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


class MintRequest(BaseModel):
    address: str
    amount: int


@router.post("/mint")
def mint(request: MintRequest):
    return token_service.mint(request.address, request.amount)


class ApproveRequest(BaseModel):
    amount: int


@router.post("/approve")
def approve(request: ApproveRequest):
    return token_service.approve(request.amount)


@router.get("/allowance")
def allowance():
    return {"allowance": token_service.allowance()}
