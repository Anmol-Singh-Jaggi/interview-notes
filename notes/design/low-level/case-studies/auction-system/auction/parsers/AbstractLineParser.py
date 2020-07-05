from abc import ABC, abstractmethod


class AbstractLineParser(ABC):
    def __init__(self, auction_system):
        self.auction_system = auction_system
        self.next_parser = None

    @abstractmethod
    def _get_command(self, line):
        pass

    def add_next_parser(self, next_parser):
        self.next_parser = next_parser
        return self.next_parser

    def parse_line(self, line):
        command = self._get_command(line)
        if command is not None:
            return command
        if command is None:
            # Chain of Responsibility Pattern
            if self.next_parser is None:
                return None
            return self.next_parser.parse_line(line)
