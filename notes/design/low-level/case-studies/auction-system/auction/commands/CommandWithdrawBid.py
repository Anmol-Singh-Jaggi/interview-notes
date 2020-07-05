from commands.AbstractCommand import AbstractCommand


class CommandWithdrawBid(AbstractCommand):
    def __init__(self, auction_system, buyer_id, auction_id):
        self.auction_system = auction_system
        self.buyer_id = buyer_id
        self.auction_id = auction_id

    def execute(self):
        return self.auction_system.withdraw_bid(self.buyer_id, self.auction_id)
