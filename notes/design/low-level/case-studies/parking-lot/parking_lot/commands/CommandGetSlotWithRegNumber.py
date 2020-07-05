from commands.AbstractCommand import AbstractCommand


class CommandGetSlotWithRegNumber(AbstractCommand):
    def __init__(self, parking_lot, reg_number):
        self.parking_lot = parking_lot
        self.reg_number = reg_number

    def execute(self):
        slot = self.parking_lot.get_slot_for_reg_number(self.reg_number)
        if slot is None:
            return 'Not found'
        return slot
