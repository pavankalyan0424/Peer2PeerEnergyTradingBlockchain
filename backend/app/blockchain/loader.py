from dataclasses import dataclass
from pathlib import Path
from typing import Any
import json

from app.core.config import CONFIG_DIR, FOUNDRY_OUT_DIR


@dataclass
class ContractArtifact:
    address: str
    abi: list[Any]


def _load_contracts_config() -> dict:
    config_path = CONFIG_DIR / "contracts.json"

    with open(config_path, "r") as config_file:
        return json.load(config_file)


def _load_address(contract_name: str) -> str:
    contracts = _load_contracts_config()

    if contract_name not in contracts:
        raise KeyError(f"{contract_name} not found in contracts.json")

    return contracts[contract_name]["address"]


def _load_abi(contract_name: str) -> list[Any]:
    artifact_path = FOUNDRY_OUT_DIR / f"{contract_name}.sol" / f"{contract_name}.json"

    with open(artifact_path, "r") as artifact_file:
        artifact = json.load(artifact_file)
        return artifact["abi"]


def load_contract(contract_name: str) -> ContractArtifact:
    return ContractArtifact(
        address=_load_address(contract_name), abi=_load_abi(contract_name)
    )
