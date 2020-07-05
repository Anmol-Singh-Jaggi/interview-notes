from parsers.AbstractLineParser import AbstractLineParser
from commands.CommandCreateAuction import CommandCreateAuction


class CommandCreateAuctionLineParser(AbstractLineParser):
    def _get_command(self, line: str):
        if not line.startswith("CREATE_AUCTION"):
            return None
        bracket_open_idx = line.index("(")
        bracket_close_idx = line.index(")")
        line = line[bracket_open_idx+1:bracket_close_idx]
        line = line.split(",")
        auction_id, lowest, highest, part_cost, seller_id = [
            word.strip('" ') for word in line
        ]
        return CommandCreateAuction(
            self.auction_system,
            auction_id,
            int(lowest),
            int(highest),
            int(part_cost),
            seller_id,
        )
