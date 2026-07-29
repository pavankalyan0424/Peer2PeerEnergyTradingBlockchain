import "./WalletSummary.css";

interface WalletSummaryProps {
    title: string;
    address: string;
    balance: number;
    allowance?:number;
}

function shortenAddress(address:string): string{
    return `${address.slice(0,6)}...${address.slice(-4)}`;
}

function WalletSummary({title,address, balance, allowance}:WalletSummaryProps){
    return (
        <div className="wallet-summary">
            <h2>{title}</h2>
            <div className="wallet-row">
                <span>Address</span>
                <strong>{shortenAddress(address)}</strong>
            </div>

            <div className="wallet-row">
                <span>Balance</span>
                <strong>{balance} ECT</strong>
            </div>

            {allowance!==undefined && (
                <div className="wallet-row">
                    <span>Allowance</span>
                    <strong>{allowance} ECT</strong>
                </div>
            )}
        </div>
    );
}
export default WalletSummary;