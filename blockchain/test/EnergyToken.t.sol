// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

import {Test} from "forge-std/Test.sol";
import {EnergyToken} from "../src/EnergyToken.sol";

contract EnergyTokenTest is Test {

		uint256 constant INITIAL_TOKEN_ALLOC = 1000 ether; //1 ether = 10^18. For simplicity we are minting in Ether

		EnergyToken token;
		address seller;
		address stranger;

		function setUp() public{
			seller = makeAddr("seller");
			stranger = makeAddr("stranger");
			token = new EnergyToken();
		}
		
		// Minting
		function testSellerGetsInitialTokens() public {
			token.mint(seller, INITIAL_TOKEN_ALLOC); // Seller joined, assign him initial tokens
			assertEq(token.balanceOf(seller), INITIAL_TOKEN_ALLOC);
		}

		function testNonOwnerCannotMint() public {
			vm.expectRevert(); //Expecting a revert as a stranger is trying to mint, which will fail
			vm.prank(stranger); //This will make msg.sender=Stranger
			token.mint(seller, INITIAL_TOKEN_ALLOC);

		}

		function testZeroAmount() public {
			vm.expectRevert("Amount must be greater than zero");
			token.mint(seller, 0);
		}


}
