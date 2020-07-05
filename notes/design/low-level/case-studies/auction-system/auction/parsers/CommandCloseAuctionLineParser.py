from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandCloseAuction import CommandCloseAuction


class CommandCloseAuctionLineParser(AbstractLineParser):
    def _get_command(self, line: str):
        if not line.startswith("CLOSE_AUCTION"):
            return None
        bracket_open_idx = line.index("(")
        bracket_close_idx = line.index(")")
        line = line[bracket_open_idx+1:bracket_close_idx]
        auction_id = line.strip('" ')
        return CommandCloseAuction(self.auction_system, auction_id)
