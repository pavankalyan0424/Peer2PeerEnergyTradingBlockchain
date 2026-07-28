from pydantic import BaseModel


class TransactionResponse(BaseModel):
    transaction_hash: str
    status: int  # 1 if Success, else 0 if Failure/Revert


class ListingResponse(BaseModel):
    listing_id: int
    seller: str
    initial_energy: int
    remaining_energy: int
    price_per_unit: int
    status: int
