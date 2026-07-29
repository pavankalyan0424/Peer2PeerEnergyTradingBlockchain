import { useState } from "react";
import { ListingStatus, type Listing } from "../../models/listing";
import { cancelListing, pruchaseEnergy } from "../../api/marketplace";
import "./ListingCard.css";


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

function shortenAddress(address:string): string{
    return `${address.slice(0,6)}...${address.slice(-4)}`;
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
        if (!window.confirm("Cancel this listing?")){
            return;
        }
        try {
            await cancelListing(listing.listingId);
            await onListingUpdate();
        } catch(error){
            console.error("Failed to cancel listing:",error);
            alert("Failed to cancel listing.");
        }
    }

    return (
        <div className="listing-card">
            <h3>Listing #{listing.listingId}</h3>
            <p className="wallet">Seller: {shortenAddress(listing.seller)}</p>
            <p>Initial Energy {listing.initialEnergy} Units</p>
            <p>Remaining Energy {listing.remainingEnergy} Units</p>
            <p>Price Per Unit {listing.pricePerUnit} ECT / Unit</p>
            <span className={`status status-${listing.status}`}>Status: {getStatus(listing.status)}</span>
            {
                listing.status === ListingStatus.ACTIVE && (
                    <>
                        <div className="purchase-section">
                            <label>Units to Purchase</label>
                            <br/>

                            <input type="number" value={purchaseUnits} onChange={(e) => setPurchaseUnits(e.target.value)} placeholder="Enter units"/>
                        </div>

                        <br />
                        <div className="button-row">
                            <button disabled={!purchaseUnits} onClick={handlePurchase}>Purchase</button>

                        <button onClick={handleCancel} className="cancel-button">
                            Cancel Listing
                        </button>
                        </div>
                    </>
                )
            }
        </div>
    );
}

export default ListingCard;
