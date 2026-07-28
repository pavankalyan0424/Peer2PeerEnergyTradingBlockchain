from pydantic import BaseModel


class TransactionResponse(BaseModel):
    transaction_hash: str
    status: int  # 1 if Success, 0 if Failure/Revert


class ListingResponse(BaseModel):
    listing_id: int
    seller: str
    initial_energy: int
    remaining_energy: int
    price_per_unit: int
    status: int


class CreateListingResponse(TransactionResponse):
    listing_id: int
    seller: str
    energy_units: int
    price_per_unit: int


class PurchaseEnergyResponse(TransactionResponse):
    listing_id: int
    buyer: str
    energy_units: int
    total_price: int


class CancelListingResponse(TransactionResponse):
    listing_id: int
    seller: str
