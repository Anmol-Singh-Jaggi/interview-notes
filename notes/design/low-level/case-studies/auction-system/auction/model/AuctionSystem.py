from model.Auction import Auction
from model.Bid import Bid
from model.Buyer import Buyer
from model.Seller import Seller
from strategies.BasicAuctionResultStrategy import BasicAuctionResultStrategy


class AuctionSystem:
    def __init__(self):
        self.sellers = {}
        self.buyers = {}
        self.auctions = {}

    def create_auction(
        self, id, lowest_possible_bid, highest_possible_bid, part_cost, seller_id, strategy=None
    ):
        auction: Auction = self.auctions.get(id, None)
        if auction is not None:
            raise Exception(f"Auction '{id}' exists already!!")
        seller: Seller = self.sellers.get(seller_id, None)
        if seller is None:
            raise Exception(f"Seller '{seller_id}' not found!!")
        if strategy is None:
            strategy = BasicAuctionResultStrategy()
        auction = Auction(
            id,
            lowest_possible_bid,
            highest_possible_bid,
            part_cost,
            seller,
            strategy,
        )
        self.auctions[id] = auction
        return auction

    def close_auction(self, auction_id):
        auction: Auction = self.auctions.get(auction_id, None)
        if auction is None:
            raise Exception(f"Auction '{auction_id}' not found!!")
        auction.close()
        return auction.winner

    def add_buyer(self, id):
        buyer = self.buyers.get(id, None)
        if buyer is not None:
            raise Exception(f"Buyer '{id}' exists already!")
        self.buyers[id] = Buyer(id)

    def add_seller(self, id):
        seller = self.sellers.get(id, None)
        if seller is not None:
            raise Exception(f"Seller '{id}' exists already!")
        self.sellers[id] = Seller(id)

    def create_bid(self, buyer_id, auction_id, amount):
        buyer = self.buyers.get(buyer_id, None)
        if buyer is None:
            raise Exception(f"Buyer '{buyer_id}' not found!")
        auction: Auction = self.auctions.get(auction_id, None)
        if auction is None:
            raise Exception(f"Auction '{auction_id}' not found!!")
        bid = Bid(buyer, auction, amount)
        try:
            return auction.register_bid(bid)
        except Exception as e:
            print(e)

    def get_profit(self, seller_id):
        seller = self.sellers.get(seller_id, None)
        if seller is None:
            raise Exception(f"Seller '{seller_id}' not found!")
        total_profit = 0
        for auction_id, auction in self.auctions.items():
            if auction.is_closed and auction.seller.id == seller_id:
                total_profit += auction.get_profit()
        return total_profit

    def withdraw_bid(self, buyer_id, auction_id):
        buyer = self.buyers.get(buyer_id, None)
        if buyer is None:
            raise Exception(f"Buyer '{buyer_id}' not found!")
        auction: Auction = self.auctions.get(auction_id, None)
        if auction is None:
            raise Exception(f"Auction '{auction_id}' not found!!")
        auction.withdraw_bid(buyer)
