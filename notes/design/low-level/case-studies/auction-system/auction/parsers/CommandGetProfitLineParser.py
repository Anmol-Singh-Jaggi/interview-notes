from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandGetProfit import CommandGetProfit


class CommandGetProfitLineParser(AbstractLineParser):
    def _get_command(self, line: str):
        if not line.startswith("GET_PROFIT"):
            return None
        bracket_open_idx = line.index("(")
        bracket_close_idx = line.index(")")
        line = line[bracket_open_idx+1:bracket_close_idx]
        seller_id = line.strip('" ')
        return CommandGetProfit(self.auction_system, seller_id)
