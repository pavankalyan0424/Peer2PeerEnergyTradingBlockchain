import api from "./api";

export async function getBalance(address:String){
    const response = await api.get(`/token/balance/${address}`);
    return response.data;
}

export async function getAllowance() {
    const response = await api.get("/token/allowance");
    return response.data;
}

export async function approveMarketplace(amount: number){
    const response = await api.post("/token/approve",{amount});
    return response.data;
}