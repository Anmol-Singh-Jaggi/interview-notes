from abc import ABC, abstractmethod
from ParkingLot import ParkingLot


class AbstractCommand(ABC):
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    @abstractmethod
    def execute(self):
        pass
