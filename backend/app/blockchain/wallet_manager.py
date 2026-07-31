from eth_account import Account

from app.blockchain.wallet import Wallet, WalletRole
from app.core.config import ADMIN_PRIVATE_KEY, BUYER_PRIVATE_KEY, SELLER_PRIVATE_KEY


class WalletManager:
    def __init__(self):
        self._wallets = {
            WalletRole.ADMIN: self._create_wallet(
                role=WalletRole.ADMIN, private_key=ADMIN_PRIVATE_KEY
            ),
            WalletRole.BUYER: self._create_wallet(
                role=WalletRole.BUYER, private_key=BUYER_PRIVATE_KEY
            ),
            WalletRole.SELLER: self._create_wallet(
                role=WalletRole.SELLER, private_key=SELLER_PRIVATE_KEY
            ),
        }

    def _create_wallet(self, role: WalletRole, private_key: str) -> Wallet:
        try:
            address = Account.from_key(private_key).address
            return Wallet(role=role, address=address, private_key=private_key)
        except Exception as error:
            raise ValueError(
                f"Invalid private key configured for {role} wallet"
            ) from error

    @property
    def admin(self) -> Wallet:
        return self._wallets[WalletRole.ADMIN]

    @property
    def buyer(self) -> Wallet:
        return self._wallets[WalletRole.BUYER]

    @property
    def seller(self) -> Wallet:
        return self._wallets[WalletRole.SELLER]


wallet_manager = WalletManager()
