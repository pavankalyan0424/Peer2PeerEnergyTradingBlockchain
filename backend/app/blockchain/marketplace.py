from app.blockchain.client import blockchain_client


class MarketplaceService:
    def __init__(self):
        self.contract = blockchain_client.get_contract("EnergyMarketplace")

    def _listing_blockchain_to_api(self, listing_id, listing):
        seller, initial, remaining, price, status = listing
        return {
            "listingId": listing_id,
            "seller": seller,
            "initialEnergy": initial,
            "remaniningEnergy": remaining,
            "pricePerUnit": price,
            "status": status,
        }

    def get_all_listings(self):
        count = self.contract.functions.getListingCount().call()
        listings = []
        for i in range(count):
            listing = self.contract.functions.listings(i).call()

            listing_resp = self._listing_blockchain_to_api(i, listing)

            if listing_resp["status"] == 0:  # NONE
                continue

            listings.append(listing_resp)
        return listings

    def get_listing(self, listing_id: int):
        listing = self.contract.functions.listings(listing_id).call()

        return self._listing_blockchain_to_api(listing_id, listing)

    def create_listing(self, energy_units: int, price_per_unit: int):
        txn = self.contract.functions.createListing(
            energy_units, price_per_unit
        ).build_transaction(
            {
                "from": blockchain_client.wallet_address,
                "nonce": blockchain_client.get_nonce(),
            }
        )

        receipt = blockchain_client.send_transaction(txn)
        return {
            "transactionHash": receipt.transactionHash.hex(),
            "status": receipt.status,
        }

    def purchase_energy(self, listing_id: int, energy_units: int):
        txn = self.contract.functions.purchaseEnergy(
            listing_id, energy_units
        ).build_transaction(
            {
                "from": blockchain_client.wallet_address,
                "nonce": blockchain_client.get_nonce(),
            }
        )

        receipt = blockchain_client.send_transaction(txn)
        return {
            "transactionHash": receipt.transactionHash.hex(),
            "status": receipt.status,
        }

    def cancel_listing(self, listing_id: int):
        txn = self.contract.functions.cancelListing(listing_id).build_transaction(
            {
                "from": blockchain_client.wallet_address,
                "nonce": blockchain_client.get_nonce(),
            }
        )

        receipt = blockchain_client.send_transaction(txn)
        return {
            "transactionHash": receipt.transactionHash.hex(),
            "status": receipt.status,
        }


marketplace_service = MarketplaceService()
