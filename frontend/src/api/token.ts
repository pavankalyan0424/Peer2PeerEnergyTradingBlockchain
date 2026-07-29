import api from "./api";

export async function mintTokens(
    recipient: string, amount: number
) {
    const response = await api.post("/token/mint", { address: recipient, amount });
    return response.data;
}
