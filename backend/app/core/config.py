from pathlib import Path
import os

RPC_URL = os.getenv("RPC_URL") or "http://localhost:8545"
ADMIN_PRIVATE_KEY = os.getenv("ADMIN_PRIVATE_KEY") or ""
SELLER_PRIVATE_KEY = os.getenv("SELLER_PRIVATE_KEY") or ""
BUYER_PRIVATE_KEY = os.getenv("BUYER_PRIVATE_KEY") or ""

BACKEND_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = BACKEND_ROOT / "config"
BLOCKCHAIN_PROJECT_ROOT = (
    BACKEND_ROOT.parent / "blockchain"
)  
FOUNDRY_OUT_DIR = BLOCKCHAIN_PROJECT_ROOT / "out"
