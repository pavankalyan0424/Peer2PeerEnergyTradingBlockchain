from pydantic import BaseModel


class CreateListingRequest(BaseModel):
    energyUnits: int
    pricePerUnit: int


class PurchaseEnergyRequest(BaseModel):
    energyUnits: int


class MintRequest(BaseModel):
    address: str
    amount: int


class ApproveRequest(BaseModel):
    amount: int
