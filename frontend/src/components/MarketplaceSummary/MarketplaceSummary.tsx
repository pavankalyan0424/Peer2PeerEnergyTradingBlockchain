import { ListingStatus, type Listing } from "../../models/listing";
import "./MarketplacSummary.css";

interface MarketplaceSummaryProps{
    listings: Listing[];
}

function MarketplaceSummary({ listings }: MarketplaceSummaryProps) {
    const total = listings.length;
    const active = listings.filter((l) => l.status === ListingStatus.ACTIVE).length;
    const soldOut = listings.filter((l) => l.status === ListingStatus.SOLD_OUT).length;
    const cancelled = listings.filter((l) => l.status === ListingStatus.CANCELLED).length;

    return (
        <div className="summary-card">
            <h2>Marketplace Summary</h2>
            <div className="summary-row"><span>Total Listings</span><strong>{total}</strong></div>
            <div className="summary-row"><span>Active</span><strong>{active}</strong></div>
            <div className="summary-row"><span>Sold Out</span><strong>{soldOut}</strong></div>
            <div className="summary-row"><span>Cancelled</span><strong>{cancelled}</strong></div>
        </div>
    )
}

export default MarketplaceSummary;
