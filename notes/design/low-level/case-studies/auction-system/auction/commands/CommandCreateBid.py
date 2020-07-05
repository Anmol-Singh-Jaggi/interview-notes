from commands.AbstractCommand import AbstractCommand


class CommandCreateBid(AbstractCommand):
    def __init__(self, auction_system, buyer_id, auction_id, amount):
        self.auction_system = auction_system
        self.buyer_id = buyer_id
        self.auction_id = auction_id
        self.amount = amount

    def execute(self):
        return self.auction_system.create_bid(self.buyer_id, self.auction_id, self.amount)
