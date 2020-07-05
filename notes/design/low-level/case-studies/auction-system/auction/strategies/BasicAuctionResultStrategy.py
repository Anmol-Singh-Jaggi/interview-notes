from strategies.AbstractAuctionResultStrategy import AbstractAuctionResultStrategy
from model import Auction


class BasicAuctionResultStrategy(AbstractAuctionResultStrategy):
    def compute_results(self, auction: Auction):
        amount_vs_bids = {}
        for bid in auction.bids:
            bids = amount_vs_bids.get(bid.amount, [])
            bids.append(bid)
            amount_vs_bids[bid.amount] = bids
        max_bid_amount = -1
        for amount, bids in amount_vs_bids.items():
            if len(bids) == 1 and amount > max_bid_amount:
                max_bid_amount = amount
        part_cost_profit_for_seller = (
            len(auction.buyers) * auction.part_cost * 0.2
        )
        auction.profit = part_cost_profit_for_seller
        if max_bid_amount == -1:
            # No winner
            return False
        else:
            bid_avg = (
                auction.lowest_possible_bid + auction.highest_possible_bid
            ) / 2
            auction.profit -= bid_avg
            auction.profit += max_bid_amount
            auction.winner = amount_vs_bids.get(max_bid_amount)[0].buyer
        return True
