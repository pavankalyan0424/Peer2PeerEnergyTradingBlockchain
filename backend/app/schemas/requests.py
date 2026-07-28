from pydantic import BaseModel


class CreateListingRequest(BaseModel):
    energy_units: int
    price_per_unit: int


class PurchaseEnergyRequest(BaseModel):
    energy_units: int


class MintRequest(BaseModel):
    address: str
    amount: int


class ApproveRequest(BaseModel):
    amount: int
