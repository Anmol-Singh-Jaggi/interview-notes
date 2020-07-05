from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandCreateBid import CommandCreateBid


class CommandCreateBidLineParser(AbstractLineParser):
    def _get_command(self, line: str):
        if not line.startswith("CREATE_BID"):
            return None
        bracket_open_idx = line.index("(")
        bracket_close_idx = line.index(")")
        line = line[bracket_open_idx+1:bracket_close_idx]
        line = line.split(",")
        buyer_id, auction_id, amount = [word.strip('" ') for word in line]
        return CommandCreateBid(self.auction_system, buyer_id, auction_id, int(amount))
