from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandStatus import CommandStatus


class CommandStatusLineParser(AbstractLineParser):
    def _get_command(self, line):
        if line.startswith('status'):
            return CommandStatus(self.parking_lot)
        return None
