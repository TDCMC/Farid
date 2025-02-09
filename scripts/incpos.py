#!/usr/bin/env python3
import argparse
import sys

program_name = "incpos"
program_version = "1.0"
def main():
    parser = argparse.ArgumentParser(
        description = "Increments the position of glyphs in the encoding"
    )
    parser.add_argument(
        "input_file",
        help = "Input .sfd file"
    )
    parser.add_argument(
        "start_pos",
        help = "Starting position for the glyphs to increment"
    )
    parser.add_argument(
        "end_pos",
        help = "End position for the glyphs to increment"
    )
    parser.add_argument(
        "output_file",
        help = "Output .sfd file (Overwrites the original file by default)",
        nargs = "?",
        default = "-"
    )
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        sfddata = file.read()

    i = args.start_pos
    ie = args.end_pos

    while i-1 != ie:
        sfddata = sfddata.replace("Encoding: "+str(ie), "Encoding: "+str(ie+1))
        ie -= 1

    if args.output_file != "-":
        with open(args.output_file, "w") as file:
            file.write(sfddata)
    else:
        with open(args.input_file, "w") as file:
            file.write(sfddata)

if __name__ == "__main__":
    sys.exit(main())