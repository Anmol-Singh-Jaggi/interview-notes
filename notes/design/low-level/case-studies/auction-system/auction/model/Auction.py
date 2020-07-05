from model.Bid import Bid
from model.Buyer import Buyer
from model.Seller import Seller
from strategies.AbstractAuctionResultStrategy import AbstractAuctionResultStrategy


class Auction:
    def __init__(
        self,
        id: int,
        lowest_possible_bid: int,
        highest_possible_bid: int,
        part_cost: int,
        seller: Seller,
        result_strategy: AbstractAuctionResultStrategy
    ):
        self.seller = seller
        self.id = id
        self.lowest_possible_bid = lowest_possible_bid
        self.highest_possible_bid = highest_possible_bid
        self.buyers = set()
        self.bids = []
        self.part_cost = part_cost
        self.profit = None
        self.is_closed = False
        self.winner = None
        self.result_strategy = result_strategy

    def close(self):
        if self.is_closed:
            raise Exception(f"Auction '{id}' already closed!!")
        self.is_closed = True
        return self.result_strategy.compute_results(self)

    def register_bid(self, bid: Bid):
        self.buyers.add(bid.buyer)
        if (
            bid.amount >= self.lowest_possible_bid
            and bid.amount <= self.highest_possible_bid
        ):
            self.bids.append(bid)
        else:
            raise Exception(
                f"Bid amount {bid} not within allowed limits [{self.lowest_possible_bid}, {self.highest_possible_bid}]!"
            )

    def withdraw_bid(self, buyer: Buyer):
        if buyer not in self.buyers:
            return
        self.buyers.remove(buyer)
        new_bids = []
        for bid in self.bids:
            if bid.buyer.id != buyer.id:
                new_bids.append(bid)
        self.bids = new_bids

    def get_profit(self):
        return self.profit

    def compute_results(self):
        return self.result_strategy.compute_results()