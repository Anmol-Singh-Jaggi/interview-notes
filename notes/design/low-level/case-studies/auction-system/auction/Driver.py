import sys
from model.AuctionSystem import AuctionSystem

from parsers.CommandAddBuyerLineParser import CommandAddBuyerLineParser
from parsers.CommandAddSellerLineParser import CommandAddSellerLineParser
from parsers.CommandCloseAuctionLineParser import CommandCloseAuctionLineParser
from parsers.CommandCreateAuctionLineParser import CommandCreateAuctionLineParser
from parsers.CommandCreateBidLineParser import CommandCreateBidLineParser
from parsers.CommandGetProfitLineParser import CommandGetProfitLineParser
from parsers.CommandWithdrawBidLineParser import CommandWithdrawBidLineParser


def create_parser_chain(auction_system):
    parser = CommandAddBuyerLineParser(auction_system)
    original_parser = parser
    parser = parser.add_next_parser(CommandAddSellerLineParser(auction_system))
    parser = parser.add_next_parser(CommandCloseAuctionLineParser(auction_system))
    parser = parser.add_next_parser(CommandCreateAuctionLineParser(auction_system))
    parser = parser.add_next_parser(CommandCreateBidLineParser(auction_system))
    parser = parser.add_next_parser(CommandGetProfitLineParser(auction_system))
    parser = parser.add_next_parser(CommandWithdrawBidLineParser(auction_system))
    return original_parser


def process_line(line, parser):
    output = None
    try:
        if line == "exit" or not line:
            return parser, output
        command = parser.parse_line(line)
        output = command.execute()
    except Exception as err:
        output = f'Invalid input "{line}": {err}'
    return parser, output


def process_file(file_name):
    auction_system = AuctionSystem()
    parser = create_parser_chain(auction_system)
    output = ""
    with open(file_name, "r") as in_file:
        for line in in_file:
            parser, line_output = process_line(line.strip(), parser)
            if line_output is None:
                continue
            output += f"{line_output}\n"
    return output


def process_stdin():
    auction_system = AuctionSystem()
    parser = create_parser_chain(auction_system)
    while True:
        try:
            line = input().strip()
            if line == "exit" or not line:
                break
            parser, output = process_line(line, parser)
            if output is None:
                continue
            print(output)
        except EOFError:
            break


def main():
    if len(sys.argv) >= 2:
        output = process_file(sys.argv[1])
        print(output, end="")
    else:
        process_stdin()


if __name__ == "__main__":
    main()
