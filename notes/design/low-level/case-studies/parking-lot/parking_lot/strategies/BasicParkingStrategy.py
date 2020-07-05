from strategies.AbstractParkingStrategy import AbstractParkingStrategy
from Car import Car


class BasicParkingStrategy(AbstractParkingStrategy):
    def __init__(self, num_slots):
        self.num_slots = num_slots
        self.slots = [None] * (num_slots + 1)
        # Could have also used a hashmap to speed up certain queries.

    def get_next_free_slot(self):
        """
        Returns the index of the next free slot.
        Returns None if no slot empty!
        """
        for slot_idx in range(1, len(self.slots)):
            car = self.slots[slot_idx]
            if car is None:
                return slot_idx
        return None

    def park(self, car: Car):
        """
        Returns None if no slot empty!
        Else, returns the slot of the parked car.
        """
        slot = self.get_next_free_slot()
        if slot is None:
            return None
        self.slots[slot] = car
        return slot

    def unpark(self, slot):
        """
        Returns the car at the slot.
        Or None if there was no car present at that slot or
        the input slot is out of range.
        """
        if slot < 1 or slot >= len(self.slots):
            return None
        car: Car = self.slots[slot]
        self.slots[slot] = None
        return car

    def get_status(self):
        status = "Slot No.    Registration No    Colour"
        for slot_idx in range(1, len(self.slots)):
            car = self.slots[slot_idx]
            if car is None:
                continue
            slot_status = (
                f"\n{str(slot_idx).ljust(12)}{str(car.reg_number).ljust(19)}{car.color}"
            )
            status += slot_status
        return status

    def get_slots_with_color(self, color):
        slots = []
        for slot_idx in range(1, len(self.slots)):
            car = self.slots[slot_idx]
            if car is None:
                continue
            if car.color == color:
                slots.append(slot_idx)
        return slots

    def get_slot_for_reg_number(self, reg_number):
        slot = None
        for slot_idx in range(1, len(self.slots)):
            car = self.slots[slot_idx]
            if car is None:
                continue
            if car.reg_number == reg_number:
                slot = slot_idx
                break
        return slot

    def get_reg_numbers_with_color(self, color):
        slots_with_color = self.get_slots_with_color(color)
        reg_numbers = []
        for slot in slots_with_color:
            car: Car = self.slots[slot]
            reg_numbers.append(car.reg_number)
        return reg_numbers
