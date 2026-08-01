import api from "./api";

export async function health() {
    const response = await api.get("/health");
    return response.data;
}

export async function blockchainStatus(){
    const response = await api.get("/blockchain/status");
    return response.data;
}