from commands.AbstractCommand import AbstractCommand


class CommandPark(AbstractCommand):
    def __init__(self, parking_lot, car):
        self.parking_lot = parking_lot
        self.car = car

    def execute(self):
        slot = self.parking_lot.park(self.car)
        if slot is None:
            output = "Sorry, parking lot is full"
        else:
            output = f"Allocated slot number: {slot}"
        return output
