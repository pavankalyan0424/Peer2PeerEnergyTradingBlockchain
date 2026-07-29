import { useState } from "react";
import { ListingStatus, type Listing } from "../models/listing";
import { cancelListing, pruchaseEnergy } from "../api/marketplace";

interface ListingCardProps {
    listing: Listing;
    onListingUpdate: () => Promise<void>;
}

function getStatus(status: ListingStatus) {
    switch (status) {
        case ListingStatus.ACTIVE:
            return "Active";
        case ListingStatus.SOLD_OUT:
            return "Sold Out";
        case ListingStatus.CANCELLED:
            return "Cancelled";
        default:
            return "Unknown";
    }
}

function ListingCard({ listing, onListingUpdate }: ListingCardProps) {
    const [purchaseUnits, setPurchaseUnits] = useState("");

    async function handlePurchase() {
        const units = Number(purchaseUnits);

        if (units <= 0) {
            alert("Purchase units must be greater than zero.");
            return;
        }

        try {
            await pruchaseEnergy(listing.listingId, units);
            await onListingUpdate();
            setPurchaseUnits("");
        } catch (error) {
            console.error("Purchase failed:", error);
            alert("Failed to purchase energy.");
        }
    }

    async function handleCancel() {
        try {
            await cancelListing(listing.listingId);
            await onListingUpdate();
        } catch(error){
            console.error("Failed to cancel listing:",error);
            alert("Failed to cancel listing.");
        }
    }

    return (
        <div>
            <h3>Listing #{listing.listingId}</h3>
            <p>Seller: {listing.seller}</p>
            <p>Initial Energy: {listing.initialEnergy}</p>
            <p>Remaining Energy: {listing.remainingEnergy}</p>
            <p>Price Per Unit: {listing.pricePerUnit}</p>
            <p>Status: {getStatus(listing.status)}</p>
            {
                listing.status === ListingStatus.ACTIVE && (
                    <>
                        <div>
                            <label>Units to Purchase</label>
                            <br />

                            <input type="number" value={purchaseUnits} onChange={(e) => setPurchaseUnits(e.target.value)} />
                        </div>

                        <br />
                        <button onClick={handlePurchase}>Purchase</button>

                        <button onClick={handleCancel} style={{margin: "10px"}}>
                            Cancel Listing
                        </button>
                    </>
                )
            }
        </div>
    );
}

export default ListingCard;
