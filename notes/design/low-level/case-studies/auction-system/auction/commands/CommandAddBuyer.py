from commands.AbstractCommand import AbstractCommand


class CommandAddBuyer(AbstractCommand):
    def __init__(self, auction_system, buyer_id):
        self.auction_system = auction_system
        self.buyer_id = buyer_id

    def execute(self):
        return self.auction_system.add_buyer(self.buyer_id)
