class MarketplaceEventDecoder:

    def __init__(self, contract):
        self.contract = contract

    def decode(self, receipt, event_name):
        event = getattr(self.contract.events, event_name)
        events = event.process_receipt(receipt)
        if not events:
            raise ValueError(f"{event_name} event not found.")

        return events[0]["args"]

    def decode_listing_created(self, receipt):
        return self.decode(receipt, "ListingCreated")

    def decode_energy_purchase(self, receipt):
        return self.decode(receipt, "EnergyPurchased")

    def decode_listing_cancelled(self, receipt):
        return self.decode(receipt, "ListingCancelled")
