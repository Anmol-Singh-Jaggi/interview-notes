from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandAddBuyer import CommandAddBuyer


class CommandAddBuyerLineParser(AbstractLineParser):
    def _get_command(self, line: str):
        if not line.startswith("ADD_BUYER"):
            return None
        bracket_open_idx = line.index("(")
        bracket_close_idx = line.index(")")
        line = line[bracket_open_idx+1:bracket_close_idx]
        buyer_id = line.strip(' "')
        return CommandAddBuyer(self.auction_system, buyer_id)
