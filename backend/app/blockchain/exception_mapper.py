from fastapi import HTTPException

ERROR_MESSAGES = {
    "CannotPurchaseOwnListing": "Cannot purchase your own listing.",
    "CannotPurchaseMoreThanRemainingUnits": "Requested energy exceeds the remaining units",
    "CannotCancelNonActiveListing": "Listing is not active",
    "InvalidEnergyUnits": "Energy Units must be greater than zero",
    "InvalidPricePerUnit": "Price Per Unit must be greater than zero",
    "ListingNotActive": "Listing is Not Active",
    "ListingNotFound": "Listing does not exist",
    "OnlySellerCanCancelListing": "Only Seller can Cancel listing",
    "PaymentFailed": "Payment Failed",
}


def map_exception(error_name):
    raise HTTPException(
        status_code=400, detail=ERROR_MESSAGES.get(error_name, error_name)
    )
