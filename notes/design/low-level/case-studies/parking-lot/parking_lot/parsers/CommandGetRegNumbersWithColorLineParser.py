from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandGetRegNumbersWithColor import CommandGetRegNumbersWithColor


class CommandGetRegNumbersWithColorLineParser(AbstractLineParser):
    def _get_command(self, line):
        if not line.startswith('registration_numbers_for_cars_with_colour'):
            return None
        _, color = line.split()
        return CommandGetRegNumbersWithColor(self.parking_lot, color)
