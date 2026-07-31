from web3 import Web3

from app.blockchain.wallet import Wallet
from app.core.config import RPC_URL
from app.blockchain.loader import load_contract
from app.schemas.responses import TransactionResponse


def txn_receipt_to_txn_response(receipt):
    return TransactionResponse(
        transaction_hash=receipt.transactionHash.hex(), status=receipt.status
    )


class BlockchainClient:

    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

    def is_connected(self):
        return self.w3.is_connected()

    def get_contract(self, contract_name: str):
        contract_artifact = load_contract(contract_name)
        return self.w3.eth.contract(
            address=contract_artifact.address, abi=contract_artifact.abi
        )

    def send_transaction(self, transaction, wallet: Wallet):
        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, wallet.private_key
        )
        txn_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        return self.w3.eth.wait_for_transaction_receipt(txn_hash)

    def get_nonce(self, wallet: Wallet):
        return self.w3.eth.get_transaction_count(wallet.address)


blockchain_client = BlockchainClient(RPC_URL)
