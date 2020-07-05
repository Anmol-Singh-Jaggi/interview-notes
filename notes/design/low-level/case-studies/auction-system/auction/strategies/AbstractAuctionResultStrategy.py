from abc import ABC, abstractmethod


class AbstractAuctionResultStrategy(ABC):
    @abstractmethod
    def compute_results(self, auction):
        pass
