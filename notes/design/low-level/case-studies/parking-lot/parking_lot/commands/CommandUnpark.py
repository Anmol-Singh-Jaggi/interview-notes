from commands.AbstractCommand import AbstractCommand


class CommandUnpark(AbstractCommand):
    def __init__(self, parking_lot, slot):
        self.parking_lot = parking_lot
        self.slot = slot

    def execute(self):
        self.parking_lot.unpark(self.slot)
        output = f'Slot number {self.slot} is free'
        return output
