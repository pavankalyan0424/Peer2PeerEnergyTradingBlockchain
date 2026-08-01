import { useState } from "react";
import { createListing } from "../../api/marketplace";
import "./CreateListingForm.css";

interface CreateListingFormProps {
    onListingCreated: () => Promise<void>;
}

function CreateListingForm({ onListingCreated }: CreateListingFormProps) {
    const [energyUnits, setEnergyUnits] = useState("");
    const [pricePerUnit, setPricePerUnit] = useState("");

    async function handleSubmit() {
        const energy = Number(energyUnits);
        const price = Number(pricePerUnit);

        if (energy <= 0 || price <= 0) {
            alert("Energy units and price must be greater than zero.");
            return;
        }

        try {
            await createListing(energy, price);

            await onListingCreated();

            setEnergyUnits("");
            setPricePerUnit("");

        } catch (error: any) {
            console.error("Failed to create listing:", error);
            const message = error.response?.data?.detail?.message ?? error.response?.data?.detail ?? "Failed to create listing.";
            alert(message);
        }

    }
    return (
        <div className="dashboard-card">
            <h2>Create New Listing</h2>
            <div>
                <label>Energy Units</label>
                <br />
                <input type="number" value={energyUnits} onChange={(e) => setEnergyUnits(e.target.value)} placeholder="Enter units" />
            </div>
            <br />

            <div>
                <label>Price Per Unit</label>
                <br />
                <input type="number" value={pricePerUnit} onChange={(e) => setPricePerUnit(e.target.value)} placeholder="Enter price" />
            </div>
            <br />

            <button onClick={handleSubmit}>Create Listing</button>
        </div>
    )
}

export default CreateListingForm;