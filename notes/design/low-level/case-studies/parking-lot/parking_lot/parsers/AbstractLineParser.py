from abc import ABC, abstractmethod


class AbstractLineParser(ABC):
    def __init__(self, parking_lot, next_parser):
        self.parking_lot = parking_lot
        self.next_parser = next_parser

    @abstractmethod
    def _get_command(self, line):
        pass

    def parse_line(self, line):
        command = self._get_command(line)
        if command is not None:
            return command
        if command is None:
            # Chain of Responsibility Pattern
            if self.next_parser is None:
                return None
            return self.next_parser.parse_line(line)
