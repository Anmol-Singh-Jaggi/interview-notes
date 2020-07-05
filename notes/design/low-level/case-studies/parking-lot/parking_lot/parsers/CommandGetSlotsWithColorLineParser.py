from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandGetSlotsWithColor import CommandGetSlotsWithColor


class CommandGetSlotsWithColorLineParser(AbstractLineParser):
    def _get_command(self, line):
        if not line.startswith('slot_numbers_for_cars_with_colour'):
            return None
        _, color = line.split()
        return CommandGetSlotsWithColor(self.parking_lot, color)
