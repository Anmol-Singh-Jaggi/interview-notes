from abc import ABC, abstractmethod
from model.AuctionSystem import AuctionSystem


class AbstractCommand(ABC):
    def __init__(self, auction_system: AuctionSystem):
        self.auction_system = auction_system

    @abstractmethod
    def execute(self):
        pass
