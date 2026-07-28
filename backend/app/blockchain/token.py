from app.blockchain.client import blockchain_client
from web3 import Web3

from app.blockchain.loader import load_contract


class TokenService:

    def __init__(self):
        self.contract = blockchain_client.get_contract("EnergyToken")

    def total_supply(self) -> int:
        supply = int(self.contract.functions.totalSupply().call())
        return supply

    def balance_of(self, address: str) -> int:
        if not Web3.is_address(address):
            raise ValueError(f"Invalid Ethereum address: {address}")

        checksum_address = Web3.to_checksum_address(address)
        balance = self.contract.functions.balanceOf(checksum_address).call()
        return int(balance)

    def mint(self, address: str, amount: int):
        txn = self.contract.functions.mint(address, amount).build_transaction(
            {
                "from": blockchain_client.wallet_address,
                "nonce": blockchain_client.get_nonce(),
            }
        )
        receipt = blockchain_client.send_transaction(txn)
        return {
            "transactionHash": receipt.transactionHash.hex(),
            "status": receipt.status,
        }

    def approve(self, amount: int):
        marketplace_address = load_contract("EnergyMarketplace").address
        txn = self.contract.functions.approve(
            marketplace_address, amount
        ).build_transaction(
            {
                "from": blockchain_client.wallet_address,
                "nonce": blockchain_client.get_nonce(),
            }
        )
        receipt = blockchain_client.send_transaction(txn)
        return {
            "transactionHash": receipt.transactionHash.hex(),
            "status": receipt.status,
        }

    def allowance(self):
        owner = blockchain_client.wallet_address
        spender = load_contract("EnergyMarketplace").address
        return self.contract.functions.allowance(owner, spender).call()


token_service = TokenService()
