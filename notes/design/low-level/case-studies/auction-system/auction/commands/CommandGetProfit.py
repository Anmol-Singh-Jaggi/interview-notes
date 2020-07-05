from commands.AbstractCommand import AbstractCommand


class CommandGetProfit(AbstractCommand):
    def __init__(self, auction_system, seller_id):
        self.auction_system = auction_system
        self.seller_id = seller_id

    def execute(self):
        return self.auction_system.get_profit(self.seller_id)
