import { useEffect, useState } from "react";
import { approveMarketplace, getAllowance, getBalance } from "../api/wallet";
import { WALLETS } from "../config/wallets";
import WalletSummary from "../components/WalletSummary/WalletSummary";

const BUYER_ADDRESS = WALLETS.buyer;


function BuyerPage() {
    const [balance, setBalance] = useState(0);
    const [allowance, setAllowance] = useState(0);
    const [approveAmount, setApproveAmount] = useState("");

    async function loadWallet() {
        try {
            const balanceResponse = await getBalance(BUYER_ADDRESS);
            const allowResponse = await getAllowance();
            setBalance(balanceResponse.balance);
            setAllowance(allowResponse.allowance);
        } catch (error) {
            console.error("Load wallet failed with error:", error);
            alert("Failed to load wallet");
        }
    }

    useEffect(() => { loadWallet() }, []);

    async function handleApprove() {
        const amount = Number(approveAmount);
        if (amount <= 0) {
            alert("Enter a valid approval amount");
            return;
        }

        try {
            await approveMarketplace(amount);
            await loadWallet();
            setApproveAmount("");
            alert("Marketplace approved successfully");
        } catch (error) {
            console.error("Approving amount failed with error:", error);
            alert("Approval failed");
        }
    }

    return (
        <>
            <WalletSummary title="Buyer Wallet" address={WALLETS.buyer} balance={balance} allowance={allowance} />
            <div className="dashboard-card">
                <h2>Approve Marketplace</h2>
                <label>Approval Amount</label>
                <input type="number" placeholder="Enter amount" value={approveAmount} onChange={(e) => setApproveAmount(e.target.value)} />
                <button onClick={handleApprove}>Approve Marketplace</button>
            </div>
        </>
    );
}

export default BuyerPage;