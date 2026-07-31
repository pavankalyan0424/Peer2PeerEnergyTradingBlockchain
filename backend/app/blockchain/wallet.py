from dataclasses import dataclass
from enum import Enum


class WalletRole(str, Enum):
    ADMIN = "admin"
    BUYER = "buyer"
    SELLER = "seller"


@dataclass(frozen=True)
class Wallet:
    role: WalletRole
    address: str
    private_key: str
