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
    "ERC20InsufficientBalance": "Buyer does not have enough ECT tokens.",
    "ERC20InsufficientAllowance": "Marketplace is not approved to spend enough ECT.",
    "ERC20InvalidSender": "Invalid sender address.",
    "ERC20InvalidReciever": "Invalid reciever address.",
    "ERC20InvalidApprover": "Invalid approver address.",
    "ERC20InvalidSpender": "Invalid spender address.",
    "InvalidAddress": "Invalid Ehtereum wallet address."
}


def map_exception(error_name):
    raise HTTPException(
        status_code=400, detail=ERROR_MESSAGES.get(error_name, error_name)
    )
