from commands.AbstractCommand import AbstractCommand


class CommandGetSlotsWithColor(AbstractCommand):
    def __init__(self, parking_lot, color):
        self.parking_lot = parking_lot
        self.color = color

    def execute(self):
        slots = self.parking_lot.get_slots_with_color(self.color)
        return ', '.join(map(str, slots))
