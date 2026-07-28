// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

import {Test} from "forge-std/Test.sol";
import {EnergyToken} from "../src/EnergyToken.sol";
import {EnergyMarketplace} from "../src/EnergyMarketplace.sol";

contract EnergyMarketplaceTest is Test {
    uint256 constant DEFAULT_ENERGY_UNITS = 25;
    uint256 constant DEFAULT_PRICE_PER_UNIT = 8;
    uint256 constant BUYER_INITIAL_BALANCE = 1000;
    uint256 constant PURCHASE_UNITS = 10;

    EnergyToken energyToken;
    EnergyMarketplace marketplace;
    address buyer;
    address seller;

    function setUp() public {
        energyToken = new EnergyToken();
        marketplace = new EnergyMarketplace(energyToken);
        buyer = makeAddr("buyer");
        seller = makeAddr("seller");
    }

    function _createDefaultListing() internal returns (uint256) {
        vm.prank(seller);
        uint256 listingId = marketplace.createListing(DEFAULT_ENERGY_UNITS, DEFAULT_PRICE_PER_UNIT);
        return listingId;
    }

    function _mintTokensToBuyer() internal {
        energyToken.mint(buyer, BUYER_INITIAL_BALANCE);
    }

    function _buyerApproveMarketplace() internal {
        vm.prank(buyer);
        energyToken.approve(address(marketplace), BUYER_INITIAL_BALANCE); // Buyer granting permission marketplace to make transfer
    }

    function testSellerCanCreateListing() public {
        uint256 listingId = _createDefaultListing();
        //vm.prank(seller);
        //uint256 listingId = marketplace.createListing(DEFAULT_ENERGY_UNITS, DEFAULT_PRICE_PER_UNIT);
        assertEq(listingId, 0);

        (
            address listingSeller,
            uint256 initialEnergy,
            uint256 remainingEnergy,
            uint256 pricePerUnit,
            EnergyMarketplace.ListingStatus status
        ) = marketplace.listings(0);

        assertEq(listingSeller, seller);
        assertEq(initialEnergy, DEFAULT_ENERGY_UNITS);
        assertEq(remainingEnergy, DEFAULT_ENERGY_UNITS);
        assertEq(pricePerUnit, DEFAULT_PRICE_PER_UNIT);
        assertEq(uint256(status), uint256(EnergyMarketplace.ListingStatus.ACTIVE));
    }

    function testSellerCreatesInvalidListingWithInvalidEnergy() public {
        vm.prank(seller);
        vm.expectRevert();
        marketplace.createListing(0, DEFAULT_PRICE_PER_UNIT);
    }

    function testSellerCreatesInvalidListingWithInvalidPrice() public {
        vm.prank(seller);
        vm.expectRevert();
        marketplace.createListing(DEFAULT_ENERGY_UNITS, 0);
    }

    function testBuyerCanPurchaseEnergy() public {
        uint256 listingId = _createDefaultListing();
        _mintTokensToBuyer();
        _buyerApproveMarketplace();
        vm.startPrank(buyer);
        marketplace.purchaseEnergy(listingId, PURCHASE_UNITS);
        vm.stopPrank();

        // check balances
        uint256 expectedCost = DEFAULT_PRICE_PER_UNIT * PURCHASE_UNITS;
        assertEq(energyToken.balanceOf(buyer), BUYER_INITIAL_BALANCE - expectedCost);
        assertEq(energyToken.balanceOf(seller), expectedCost);
    }

    function testCannotPurchaseZeroUnits() public {
        uint256 listingId = _createDefaultListing();
        _mintTokensToBuyer();
        _buyerApproveMarketplace();
        vm.expectRevert(EnergyMarketplace.InvalidEnergyUnits.selector);
        vm.prank(buyer);
        marketplace.purchaseEnergy(listingId, 0);
    }

    function testSellerCannotPurchaseOwnListing() public {
        uint256 listingId = _createDefaultListing();
        _mintTokensToBuyer();
        _buyerApproveMarketplace();
        vm.expectRevert(EnergyMarketplace.CannotPurchaseOwnListing.selector);
        vm.prank(seller);
        marketplace.purchaseEnergy(listingId, PURCHASE_UNITS);
    }

    function testCannotPurchaseMoreThanRemainingEnergy() public {
        uint256 listingId = _createDefaultListing();
        _mintTokensToBuyer();
        _buyerApproveMarketplace();
        vm.expectRevert(EnergyMarketplace.CannotPurchaseMoreThanRemainingUnits.selector);
        vm.prank(buyer);
        marketplace.purchaseEnergy(listingId, PURCHASE_UNITS + DEFAULT_ENERGY_UNITS);
    }

    function testCannotPurchaseInactiveListing() public {
        uint256 listingId = _createDefaultListing();
        _mintTokensToBuyer();
        _buyerApproveMarketplace();
        vm.prank(buyer);
        marketplace.purchaseEnergy(listingId, DEFAULT_ENERGY_UNITS);
        vm.expectRevert(EnergyMarketplace.ListingNotActive.selector);
        vm.prank(buyer);
        marketplace.purchaseEnergy(listingId, 1);
    }

    function testPurchaseFailsWithoutApproval() public {
        uint256 listingId = _createDefaultListing();
        _mintTokensToBuyer();
        vm.expectRevert();
        vm.prank(buyer);
        marketplace.purchaseEnergy(listingId, PURCHASE_UNITS);
    }

    function testSellerCanCanelListing() public {
        uint256 listingId = _createDefaultListing();
        vm.prank(seller);
        marketplace.cancelListing(listingId);
    }

    function testNonSellerCannotCancelListing() public {
        uint256 listingId = _createDefaultListing();
        vm.prank(buyer);
        vm.expectRevert(EnergyMarketplace.OnlySellerCanCancelListing.selector);
        marketplace.cancelListing(listingId);
    }

    function testCannotCancelSoldOutListing() public {
        uint256 listingId = _createDefaultListing();
        _mintTokensToBuyer();
        _buyerApproveMarketplace();
        vm.prank(buyer);
        marketplace.purchaseEnergy(listingId, DEFAULT_ENERGY_UNITS);
        vm.prank(seller);
        vm.expectRevert(EnergyMarketplace.CannotCancelNonActiveListing.selector);
        marketplace.cancelListing(listingId);
    }

    function testCannotCancelAlreadyCancelledListing() public {
        uint256 listingId = _createDefaultListing();
        vm.startPrank(seller);
        marketplace.cancelListing(listingId);
        vm.expectRevert(EnergyMarketplace.CannotCancelNonActiveListing.selector);
        marketplace.cancelListing(listingId);
        vm.stopPrank();
    }

    function testSellerTryingToCancelNotExistingListing() public {
        uint256 listingId = 100;
        vm.prank(seller);
        vm.expectRevert(EnergyMarketplace.ListingNotFound.selector);
        marketplace.cancelListing(listingId);
    }
}
