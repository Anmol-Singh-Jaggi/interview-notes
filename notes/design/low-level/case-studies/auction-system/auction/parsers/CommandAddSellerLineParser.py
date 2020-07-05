from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandAddSeller import CommandAddSeller


class CommandAddSellerLineParser(AbstractLineParser):
    def _get_command(self, line: str):
        if not line.startswith("ADD_SELLER"):
            return None
        bracket_open_idx = line.index("(")
        bracket_close_idx = line.index(")")
        line = line[bracket_open_idx+1:bracket_close_idx]
        seller_id = line.strip(' "')
        return CommandAddSeller(self.auction_system, seller_id)
