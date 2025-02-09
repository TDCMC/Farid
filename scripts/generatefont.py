#!/usr/bin/env python3
import fontforge
import argparse
import sys

program_name = "generatefont"
program_version = "1.0"

def main():
    parser = argparse.ArgumentParser(
        description = "Generates a font from a .sfd file."
    )
    parser.add_argument(
        "input_file",
        help = "Input .sfd file"
    )
    parser.add_argument(
        "output_file",
        help = "Output font file",
        nargs = "?",
        default = "-"
    )
    args = parser.parse_args()

    try:
        FontSfd = fontforge.open(args.input_file)
    except:
        parser.print_help()
        return 1
    
    if args.output_file != "-":
        FontSfd.generate(args.output_file)
    else:
        FontSfd.generate(args.input_file.replace("sfd", "ttf"))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
