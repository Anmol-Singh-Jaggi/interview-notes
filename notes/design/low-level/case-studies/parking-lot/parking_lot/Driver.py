import sys
from ParkingLot import ParkingLot
from parsers.CommandStatusLineParser import CommandStatusLineParser
from parsers.CommandGetRegNumbersWithColorLineParser import (
    CommandGetRegNumbersWithColorLineParser,
)
from parsers.CommandGetSlotsWithColorLineParser import (
    CommandGetSlotsWithColorLineParser,
)
from parsers.CommandGetSlotWithRegNumberLineParser import (
    CommandGetSlotWithRegNumberLineParser,
)
from parsers.CommandParkLineParser import CommandParkLineParser
from parsers.CommandUnparkLineParser import CommandUnparkLineParser
from strategies.BasicParkingStrategy import BasicParkingStrategy


def create_parser_chain(parking_lot):
    parser = CommandStatusLineParser(parking_lot, None)
    parser = CommandGetRegNumbersWithColorLineParser(parking_lot, parser)
    parser = CommandGetSlotsWithColorLineParser(parking_lot, parser)
    parser = CommandGetSlotWithRegNumberLineParser(parking_lot, parser)
    parser = CommandParkLineParser(parking_lot, parser)
    parser = CommandUnparkLineParser(parking_lot, parser)
    return parser


def process_create_line(line):
    _, num_slots = line.split()
    strategy = BasicParkingStrategy(int(num_slots))
    parking_lot = ParkingLot(strategy)
    output = f"Created a parking lot with {num_slots} slots"
    parser = create_parser_chain(parking_lot)
    return parser, output


def process_line(line, parser):
    output = None
    try:
        if line == "exit" or not line:
            return parser, output
        elif parser is None:
            parser, output = process_create_line(line)
        else:
            command = parser.parse_line(line)
            output = command.execute()
    except Exception as err:
        output = f'Invalid input "{line}": {err}'
    return parser, output


def process_file(file_name):
    parser = None
    output = ""
    with open(file_name, "r") as in_file:
        for line in in_file:
            parser, line_output = process_line(line.strip(), parser)
            if line_output is None:
                continue
            output += f'{line_output}\n'
    return output


def process_stdin():
    parser = None
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
