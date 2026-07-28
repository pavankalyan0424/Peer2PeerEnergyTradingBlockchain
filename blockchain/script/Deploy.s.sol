// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

import "forge-std/Script.sol";
import "forge-std/console2.sol";
import "../src/EnergyToken.sol";
import "../src/EnergyMarketplace.sol";

contract Deploy is Script {
    function run() external {
        vm.startBroadcast();
        EnergyToken token = new EnergyToken();
        EnergyMarketplace marketplace = new EnergyMarketplace(token);
        console2.log("EnergeToken is deployed at: ", address(token));
        console2.log("EnergyMarketplace is deployed at: ", address(marketplace));
        vm.stopBroadcast();
    }
}

