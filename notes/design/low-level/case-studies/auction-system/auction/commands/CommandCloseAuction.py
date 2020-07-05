from commands.AbstractCommand import AbstractCommand


class CommandCloseAuction(AbstractCommand):
    def __init__(self, auction_system, auction_id):
        self.auction_system = auction_system
        self.auction_id = auction_id

    def execute(self):
        return self.auction_system.close_auction(self.auction_id)
