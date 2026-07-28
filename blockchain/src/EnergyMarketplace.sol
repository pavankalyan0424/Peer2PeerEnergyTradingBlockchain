// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract EnergyMarketplace {
    IERC20 public immutable energyToken;

    constructor(IERC20 _energyToken) {
        energyToken = _energyToken;
    }

    enum ListingStatus {
        NONE,
        ACTIVE,
        SOLD_OUT,
        CANCELLED
    }

    struct EnergyListing {
        address seller;
        uint256 initialEnergy;
        uint256 remainingEnergy;
        uint256 pricePerUnit;
        ListingStatus status;
    }

    error InvalidEnergyUnits();
    error InvalidPricePerUnit();
    error CannotPurchaseOwnListing();
    error PaymentFailed();
    error ListingNotActive();
    error CannotPurchaseMoreThanRemainingUnits();
    error OnlySellerCanCancelListing();
    error CannotCancelNonActiveListing();
    error ListingNotFound();

    mapping(uint256 => EnergyListing) public listings;

    uint256 private nextListingId;

    event ListingCreated(uint256 indexed ListingId, address indexed seller, uint256 energyUnits, uint256 pricePerUnit);

    event EnergyPurchased(uint256 indexed listingId, address indexed buyer, uint256 energyUnits, uint256 totalPrice);

    event ListingCancelled(uint256 indexed listingId, address indexed seller);

    function getListingCount() external view returns (uint256) {
        return nextListingId;
    }

    function createListing(uint256 energyUnits, uint256 pricePerUnit) external returns (uint256) {
        if (energyUnits == 0) {
            revert InvalidEnergyUnits();
        }
        if (pricePerUnit == 0) {
            revert InvalidPricePerUnit();
        }
        uint256 listingId = nextListingId;
        listings[listingId] = EnergyListing({
            seller: msg.sender,
            initialEnergy: energyUnits,
            remainingEnergy: energyUnits,
            pricePerUnit: pricePerUnit,
            status: ListingStatus.ACTIVE
        });

        nextListingId++;

        emit ListingCreated(listingId, msg.sender, energyUnits, pricePerUnit);

        return listingId;
    }

    function purchaseEnergy(uint256 listingId, uint256 energyUnits) external {
        if (energyUnits == 0) {
            revert InvalidEnergyUnits();
        }

        EnergyListing storage listing = listings[listingId];
        if (listing.status != ListingStatus.ACTIVE) {
            revert ListingNotActive();
        }
        if (msg.sender == listing.seller) {
            revert CannotPurchaseOwnListing();
        }
        if (listing.remainingEnergy < energyUnits) {
            revert CannotPurchaseMoreThanRemainingUnits();
        }
        uint256 totalPrice = energyUnits * listing.pricePerUnit;
        bool success = energyToken.transferFrom(msg.sender, listing.seller, totalPrice);
        if (!success) {
            revert PaymentFailed();
        }

        listing.remainingEnergy = listing.remainingEnergy - energyUnits;
        if (listing.remainingEnergy == 0) {
            listing.status = ListingStatus.SOLD_OUT;
        }

        emit EnergyPurchased(listingId, msg.sender, energyUnits, totalPrice);
    }

    function cancelListing(uint256 listingId) external {
        EnergyListing storage listing = listings[listingId];
        if (listing.status == ListingStatus.NONE) {
            revert ListingNotFound();
        }
        if (listing.status != ListingStatus.ACTIVE) {
            revert CannotCancelNonActiveListing();
        }
        if (msg.sender != listing.seller) {
            revert OnlySellerCanCancelListing();
        }
        listing.status = ListingStatus.CANCELLED;
        emit ListingCancelled(listingId, msg.sender);
    }
}

