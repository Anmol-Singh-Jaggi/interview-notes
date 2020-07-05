from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandUnpark import CommandUnpark


class CommandUnparkLineParser(AbstractLineParser):
    def _get_command(self, line):
        if not line.startswith("leave"):
            return None
        _, slot = line.split()
        return CommandUnpark(self.parking_lot, int(slot))
