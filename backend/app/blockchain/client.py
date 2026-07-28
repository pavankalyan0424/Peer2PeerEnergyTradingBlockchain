from web3 import Web3

from app.core.config import RPC_URL, PRIVATE_KEY
from app.blockchain.loader import load_contract


class BlockchainClient:

    def __init__(self, rpc_url: str, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self._private_key = PRIVATE_KEY
        self.account = self.w3.eth.account.from_key(private_key)
        self.wallet_address = self.account.address

    def is_connected(self):
        return self.w3.is_connected()

    def get_contract(self, contract_name: str):
        contract_artifact = load_contract(contract_name)
        return self.w3.eth.contract(
            address=contract_artifact.address, abi=contract_artifact.abi
        )

    def send_transaction(self, transaction):
        signed_tx = self.w3.eth.account.sign_transaction(transaction, self._private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def get_nonce(self):
        return self.w3.eth.get_transaction_count(self.wallet_address)


blockchain_client = BlockchainClient(RPC_URL, PRIVATE_KEY)
