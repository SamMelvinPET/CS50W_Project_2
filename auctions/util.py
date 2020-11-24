from decimal import Decimal


def get_min_bid(listing):
    if listing.bidder:
        minbid = listing.bid + Decimal(0.01)
    else:
        minbid = listing.bid
    return minbid