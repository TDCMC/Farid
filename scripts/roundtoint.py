#!/usr/bin/env python3
import fontforge
import argparse
import sys

program_name = "roundtoint"
program_version = "1.0"

def main():
    parser = argparse.ArgumentParser(
        description = "Rounds every glyph in a .sfd file to int."
    )
    parser.add_argument(
        "input_file",
        help = "Input .sfd file"
    )
    parser.add_argument(
        "output_file",
        help = "Output .sfd file (Overwrites the original file by default)",
        nargs = "?",
        default = "-"
    )
    args = parser.parse_args()

    try:
        FontSfd = fontforge.open(args.input_file)
        for glyph in FontSfd.glyphs():
            glyph.round()
    except:
        parser.print_help()
        return 1

    if args.output_file != "-":
        FontSfd.save(args.output_file)
    else:
        FontSfd.save(args.input_file)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
