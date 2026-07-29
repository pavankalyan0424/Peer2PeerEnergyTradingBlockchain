from enum import IntEnum

from app.blockchain.client import txn_receipt_to_txn_response
from app.blockchain.event_decoder import MarketplaceEventDecoder
from app.schemas.responses import (
    CancelListingResponse,
    CreateListingResponse,
    ListingResponse,
    PurchaseEnergyResponse,
)
from app.services.base_blockchain_service import BaseBlockchainService


class ListingStatus(IntEnum):
    NONE = 0
    ACTIVE = 1
    SOLD_OUT = 2
    CANCELLED = 3


class MarketplaceService(BaseBlockchainService):
    def __init__(self):
        contract_name = "EnergyMarketplace"
        super().__init__(contract_name)
        self.event_decoder = MarketplaceEventDecoder(self.contract)

    def _listing_blockchain_to_api(self, listing_id, listing):
        seller, initial, remaining, price, status = listing
        return ListingResponse(
            listingId=listing_id,
            seller=seller,
            initialEnergy=initial,
            remainingEnergy=remaining,
            pricePerUnit=price,
            status=status,
        )

    def get_all_listings(self):
        count = self.contract.functions.getListingCount().call()
        listings = []
        for i in range(count):
            listing = self.contract.functions.listings(i).call()

            listing_resp = self._listing_blockchain_to_api(i, listing)

            if listing_resp.status == ListingStatus.NONE:  # NONE
                continue

            listings.append(listing_resp)
        return listings

    def get_listing(self, listing_id: int):
        listing = self.contract.functions.listings(listing_id).call()
        return self._listing_blockchain_to_api(listing_id, listing)

    def create_listing(self, energy_units: int, price_per_unit: int):
        receipt = self._execute_contract_function(
            self.contract.functions.createListing(energy_units, price_per_unit)
        )
        event = self.event_decoder.decode_listing_created(receipt)
        return CreateListingResponse(
            listingId=event["listingId"],
            seller=event["seller"],
            energyUnits=event["energyUnits"],
            pricePerUnit=event["energyUnits"],
            transaction_hash=receipt.transactionHash.hex(),
            status=receipt.status,
        )

    def purchase_energy(self, listing_id: int, energy_units: int):
        receipt = self._execute_contract_function(
            self.contract.functions.purchaseEnergy(listing_id, energy_units)
        )
        event = self.event_decoder.decode_energy_purchase(receipt)
        return PurchaseEnergyResponse(
            listingId=event["listingId"],
            buyer=event["buyer"],
            energyUnits=event["energyUnits"],
            totalPrice=event["totalPrice"],
            transaction_hash=receipt.transactionHash.hex(),
            status=receipt.status,
        )

    def cancel_listing(self, listing_id: int):
        receipt = self._execute_contract_function(
            self.contract.functions.cancelListing(listing_id)
        )
        event = self.event_decoder.decode_listing_cancelled(receipt)
        return CancelListingResponse(
            listingId=event["listingId"],
            seller=event["seller"],
            transaction_hash=receipt.transactionHash.hex(),
            status=receipt.status,
        )


marketplace_service = MarketplaceService()
