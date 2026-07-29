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

        } catch (error) {
            console.error("Failed to create listing:", error);
            alert("Failed to create listing.");
        }

    }
    return (
        <div className="dashboard-card">
            <h2>Create New Listing</h2>
            <div>
                <label>Energy Units</label>
                <br />
                <input type="number" value={energyUnits} onChange={(e) => setEnergyUnits(e.target.value)} />
            </div>
            <br />

            <div>
                <label>Price Per Unit</label>
                <br />
                <input type="number" value={pricePerUnit} onChange={(e) => setPricePerUnit(e.target.value)} />
            </div>
            <br />

            <button onClick={handleSubmit}>Create Listing</button>
        </div>
    )
}

export default CreateListingForm;