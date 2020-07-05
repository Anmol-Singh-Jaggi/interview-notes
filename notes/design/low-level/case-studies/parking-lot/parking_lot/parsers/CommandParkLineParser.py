from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandPark import CommandPark
from Car import Car


class CommandParkLineParser(AbstractLineParser):
    def _get_command(self, line):
        if not line.startswith('park'):
            return None
        _, reg_num, color = line.split()
        car = Car(color, reg_num)
        return CommandPark(self.parking_lot, car)
