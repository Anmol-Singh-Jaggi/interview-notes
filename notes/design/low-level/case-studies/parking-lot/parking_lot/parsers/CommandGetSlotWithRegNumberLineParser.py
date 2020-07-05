from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandGetSlotWithRegNumber import CommandGetSlotWithRegNumber


class CommandGetSlotWithRegNumberLineParser(AbstractLineParser):
    def _get_command(self, line):
        if not line.startswith('slot_number_for_registration_number'):
            return None
        _, reg_number = line.split()
        return CommandGetSlotWithRegNumber(self.parking_lot, reg_number)
