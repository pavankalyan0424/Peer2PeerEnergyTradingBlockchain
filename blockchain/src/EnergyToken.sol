// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

contract EnergyToken is ERC20,Ownable {
	
	// Constructor body is empty, as mint happens when new user is signed up to system
	constructor()
		ERC20("Enerchain Energy Token", "ECT")
		Ownable(msg.sender)
	{}
	
	/// @notice Mint ECT tokens to a registered user
	/// @dev Only the platform owner/admin can mint new tokens - As Admin/Backend will be invoking.
	function mint(address to, uint256 amount) external onlyOwner {
		require(amount > 0, "Amount must be greater than zero");
		_mint(to, amount);
	}
}
