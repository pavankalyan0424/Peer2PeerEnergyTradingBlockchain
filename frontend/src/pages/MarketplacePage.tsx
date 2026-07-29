import { useEffect, useState } from "react";
import { getListings } from "../api/marketplace";
import { type Listing } from "../models/listing";
import ListingCard from "../components/ListingCard/ListingCard";
import CreateListingForm from "../components/CreateListingForm/CreateListingForm";
import "../pages/MarketplacePage.css";
import MarketplaceSummary from "../components/MarketplaceSummary/MarketplaceSummary";


function MarketplacePage() {
    const [listings, setListings] = useState<Listing[]>([]);

    async function loadListings() {
        try {
            const data = await getListings();
            setListings(data);
        } catch (error) {
            console.error("Failed to load listings:", error);
        }
    }

    useEffect(() => { loadListings(); }, []);

    return (
        <div className="marketplace-page">
            <h2>Peer-to-Peer Energy Trading Marketplace</h2>

            <div className="marketplace-header">
                <MarketplaceSummary listings={listings} />
                <CreateListingForm onListingCreated={loadListings} />
            </div>

            <div className="listing-grid">
                {listings.map((listing) => (
                    <ListingCard key={listing.listingId} listing={listing} onListingUpdate={loadListings} />
                ))}
            </div>
        </div>
    );

}

export default MarketplacePage;
