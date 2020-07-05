from commands.AbstractCommand import AbstractCommand


class CommandAddSeller(AbstractCommand):
    def __init__(self, auction_system, seller_id):
        self.auction_system = auction_system
        self.seller_id = seller_id

    def execute(self):
        return self.auction_system.add_seller(self.seller_id)
