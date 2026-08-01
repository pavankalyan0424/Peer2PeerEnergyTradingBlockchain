from eth_utils import keccak

from app.blockchain.loader import load_contract


class ErrorDecoder:

    def __init__(self):
        self.error_selectors = {}
        for contract_name in ["EnergyMarketplace", "EnergyToken"]:
            self._register_contract(contract_name)

    def _register_contract(self, contract_name):
        abi = load_contract(contract_name).abi
        self.error_selectors.update(self._build_error_map(abi))

    def _build_error_map(self, abi):
        error_map = {}

        for item in abi:
            if item.get("type") != "error":
                continue

            input_types = ",".join(inp["type"] for inp in item.get("inputs", []))
            signature = f'{item["name"]}({input_types})'
            selector = "0x" + keccak(text=signature)[:4].hex()
            error_map[selector] = item["name"]
        return error_map

    def decode(self, selector):
        return self.error_selectors.get(selector, "UnknownBlockchainError")
