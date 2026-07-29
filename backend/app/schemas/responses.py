from pydantic import BaseModel


class TransactionResponse(BaseModel):
    transaction_hash: str
    status: int  # 1 if Success, 0 if Failure/Revert


class ListingResponse(BaseModel):
    listingId: int
    seller: str
    initialEnergy: int
    remainingEnergy: int
    pricePerUnit: int
    status: int


class CreateListingResponse(TransactionResponse):
    listingId: int
    seller: str
    energyUnits: int
    pricePerUnit: int


class PurchaseEnergyResponse(TransactionResponse):
    listingId: int
    buyer: str
    energyUnits: int
    totalPrice: int


class CancelListingResponse(TransactionResponse):
    listingId: int
    seller: str
