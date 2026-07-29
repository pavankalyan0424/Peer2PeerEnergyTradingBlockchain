import { useEffect, useState } from "react";
import { getListings } from "../api/marketplace";
import { type Listing } from "../models/listing";
import ListingCard from "../components/ListingCard";
import CreateListingForm from "../components/CreateListingForm";



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
        <div>
            <h1>EnerChain</h1>

            <h2>Peer-to-Peer Energy Trading Marketplace</h2>

            <CreateListingForm onListingCreated={loadListings} />

            <p>Total Listings: {listings.length}</p>

            {listings.map((listing) => (
                <ListingCard key={listing.listingId} listing={listing} onListingUpdate={loadListings} />
            ))}
        </div>
    )

}

export default MarketplacePage;
