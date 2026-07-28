# Marketplace APIs
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.blockchain.client import blockchain_client
from app.blockchain.marketplace import ListingStatus, marketplace_service
from app.schemas.requests import CreateListingRequest, PurchaseEnergyRequest
from app.schemas.responses import ListingResponse, TransactionResponse

router = APIRouter(prefix="/marketplace", tags=["Marketplace"])


@router.post("/listings", response_model=TransactionResponse)
def create_listing(request: CreateListingRequest):
    try:
        return marketplace_service.create_listing(
            request.energy_units, request.price_per_unit
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/listings", response_model=list[ListingResponse])
def get_all_listings():
    return marketplace_service.get_all_listings()


@router.get("/listings/{listing_id}", response_model=ListingResponse)
def get_listing(listing_id: int):
    try:
        listing = marketplace_service.get_listing(listing_id)
        # Mapping in Solidity never tells if a key exists. If a key that is accessed that has never been writtern, then Solidity returns the default value for every field.
        if listing.status == ListingStatus.NONE:  # ListingStatus.None
            raise HTTPException(
                status_code=404, detail=f"Listing {listing_id} does not exist"
            )
        return listing
    except HTTPException:
        # Re-raise these exceptions
        raise
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/listings/{listing_id}/purchase", response_model=TransactionResponse)
def purchase_energy(listing_id: int, request: PurchaseEnergyRequest):
    try:
        return marketplace_service.purchase_energy(listing_id, request.energy_units)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/listings/{listing_id}/cancel", response_model=TransactionResponse)
def cancel_listing(listing_id: int):
    return marketplace_service.cancel_listing(listing_id)
