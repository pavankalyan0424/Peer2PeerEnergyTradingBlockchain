import type { Listing } from "../models/listing";
import api from "./api";

export async function getListings(): Promise<Listing[]> {
    const response = await api.get<Listing[]>("/marketplace/listings");
    return response.data
}

export async function createListing(energyUnits: number, pricePerUnit: number){
    const response = await api.post("/marketplace/listings", {
        energyUnits,pricePerUnit
    });
    return response.data;
}

export async function pruchaseEnergy(listingId:number, energyUnits:number){
    const response = await api.post(
        `/marketplace/listings/${listingId}/purchase`,
        {
            energyUnits
        }
    );
    return response.data;
}

export async function cancelListing(listingId: number){
    const response = await api.post(
        `/marketplace/listings/${listingId}/cancel`,
    );
    return response.data;
}