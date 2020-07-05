from Car import Car


class ParkingLot:
    def __init__(self, strategy):
        self.strategy = strategy

    def get_next_free_slot(self):
        return self.strategy.get_next_free_slot()

    def park(self, car: Car):
        return self.strategy.park(car)

    def unpark(self, slot):
        return self.strategy.unpark(slot)

    def get_status(self):
        return self.strategy.get_status()

    def get_slots_with_color(self, color):
        return self.strategy.get_slots_with_color(color)

    def get_slot_for_reg_number(self, reg_number):
        return self.strategy.get_slot_for_reg_number(reg_number)

    def get_reg_numbers_with_color(self, color):
        return self.strategy.get_reg_numbers_with_color(color)
