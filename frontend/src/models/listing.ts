export const ListingStatus = {
    NONE: 0, ACTIVE: 1, SOLD_OUT: 2, CANCELLED: 3
} as const;

export type ListingStatus = (typeof ListingStatus)[keyof typeof ListingStatus];

export interface Listing {
    listingId: number;
    seller: string;
    initialEnergy: number;
    remainingEnergy: number;
    pricePerUnit: number;
    status: ListingStatus;
}