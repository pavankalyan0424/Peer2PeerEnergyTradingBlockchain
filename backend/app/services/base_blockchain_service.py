from app.blockchain.client import blockchain_client
from app.blockchain.error_decoder import ErrorDecoder
from app.blockchain.exception_mapper import map_exception
from web3.exceptions import ContractCustomError

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseBlockchainService:

    def __init__(self, contract_name):
        self.contract = blockchain_client.get_contract(contract_name)
        self.error_decoder = ErrorDecoder(self.contract.abi)

    def _execute_contract_function(self, contract_function):
        try:
            txn = contract_function.build_transaction(
                {
                    "from": blockchain_client.wallet_address,
                    "nonce": blockchain_client.get_nonce(),
                }
            )
            receipt = blockchain_client.send_transaction(txn)
            logger.info(
                "Transaction mined | fn = %s | hash = %s | status = %s",
                contract_function.fn_name,
                receipt.transactionHash.hex(),
                receipt.status,
            )
            return receipt
        except ContractCustomError as e:
            selector = e.args[0]
            error_name = self.error_decoder.decode(selector)
            map_exception(error_name)
        except Exception:
            logger.exception(
                "Transaction failed while executing %s", contract_function.fn_name
            )
            raise
