import { useEffect, useState } from "react";
import { blockchainStatus, health } from "../../api/system";

function SystemStatus() {
    const [backend, setBackend] = useState(false);
    const [blockchain, setBlockchain]= useState(false);

    async function loadStatus() {
        try {
            await health();
            setBackend(true);
        }
        catch{
            setBackend(false);
        }

        try {
            const response = await blockchainStatus();
            setBlockchain(response.connected);
        }
        catch{
            setBackend(false);
        }
    }

    useEffect(() => {
        loadStatus();
        const timer = setInterval(loadStatus,15000);
        return () => clearInterval(timer);
    },[]);

    return (
        <div className="system-status">
            <span>{backend ? "🟢" : "🔴"} Backend</span>
             <span>{blockchain ? "🟢" : "🔴"} Blockchain</span>
        </div>
    );
}

export default SystemStatus;