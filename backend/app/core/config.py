from pathlib import Path
import os

RPC_URL = os.getenv("RPC_URL") or "http://localhost:8545"
PRIVATE_KEY = (
    os.getenv("PRIVATE_KEY")
    or ""
)  # TODO: remove PRIVATEKEY value

BACKEND_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = BACKEND_ROOT / "config"
BLOCKCHAIN_PROJET_ROOT = (
    BACKEND_ROOT.parent / "blockchain_docker"
)  # TODO: rename this later
FOUNDRY_OUT_DIR = BLOCKCHAIN_PROJET_ROOT / "out"
