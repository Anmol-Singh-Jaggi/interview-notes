from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandWithdrawBid import CommandWithdrawBid


class CommandWithdrawBidLineParser(AbstractLineParser):
    def _get_command(self, line: str):
        if not line.startswith("WITHDRAW_BID"):
            return None
        bracket_open_idx = line.index("(")
        bracket_close_idx = line.index(")")
        line = line[bracket_open_idx+1:bracket_close_idx]
        line = line.split(",")
        buyer_id, auction_id = [word.strip('" ') for word in line]
        return CommandWithdrawBid(self.auction_system, buyer_id, auction_id)
