from commands.AbstractCommand import AbstractCommand


class CommandCreateAuction(AbstractCommand):
    def __init__(
        self,
        auction_system,
        auction_id,
        lowest_possible_bid,
        highest_possible_bid,
        part_cost,
        seller_id,
    ):
        self.auction_system = auction_system
        self.auction_id = auction_id
        self.lowest_possible_bid = lowest_possible_bid
        self.highest_possible_bid = highest_possible_bid
        self.part_cost = part_cost
        self.seller_id = seller_id

    def execute(self):
        return self.auction_system.create_auction(
            self.auction_id,
            self.lowest_possible_bid,
            self.highest_possible_bid,
            self.part_cost,
            self.seller_id,
        )
