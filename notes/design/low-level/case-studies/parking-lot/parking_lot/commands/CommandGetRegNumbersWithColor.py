from commands.AbstractCommand import AbstractCommand


class CommandGetRegNumbersWithColor(AbstractCommand):
    def __init__(self, parking_lot, color):
        self.parking_lot = parking_lot
        self.color = color

    def execute(self):
        reg_numbers = self.parking_lot.get_reg_numbers_with_color(self.color)
        output = ', '.join(reg_numbers)
        return output
