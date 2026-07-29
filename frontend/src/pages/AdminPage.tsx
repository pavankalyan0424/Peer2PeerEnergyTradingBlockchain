import { useState } from "react";
import { mintTokens } from "../api/token";
import WalletSummary from "../components/WalletSummary/WalletSummary";
import { WALLETS } from "../config/wallets";

function AdminPage(){
    const [recipient, setRecipient] = useState("");
    const [amount, setAmount] = useState("");

    async function handleMint(){
        if(!recipient|| Number(amount) <=0){
            alert("Please enter a valid recipient and amount");
            return ;
        }

        try{
            await mintTokens(recipient,Number(amount));
            alert("Tokens minted successfully");

            setRecipient("");
            setAmount("");

        }
        catch(error){
            console.error("Minting failed with error:",error);
            alert("Mint failed");
        }
    }

    return (
        <>
        <WalletSummary title="Admin Wallet" address={WALLETS.admin} balance={0}/>
        <div className="dashboard-card">
            <h2>Admin Dashboard</h2>
            <p>Mint Energy tokens</p>
            <hr/>
            <p>Only the contract owner can mint new ECT Tokens</p>
            <label>Recipient Address</label>
            <input value={recipient} onChange={(e) => setRecipient(e.target.value)} placeholder="Enter Recipient Address"/>
            <label>Amount</label>
            <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Enter Amount"/>
            <button onClick={handleMint}>Mint Tokens</button>
        </div>
        </>
    );
}

export default AdminPage;