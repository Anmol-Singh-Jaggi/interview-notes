from abc import ABC, abstractmethod


class AbstractParkingStrategy(ABC):
    @abstractmethod
    def __init__(self, num_slots):
        pass

    @abstractmethod
    def get_next_free_slot(self):
        pass

    @abstractmethod
    def park(self, car):
        pass

    @abstractmethod
    def unpark(self, slot):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_slots_with_color(self, color):
        pass

    @abstractmethod
    def get_slot_for_reg_number(self, reg_number):
        pass

    @abstractmethod
    def get_reg_numbers_with_color(self, color):
        pass
