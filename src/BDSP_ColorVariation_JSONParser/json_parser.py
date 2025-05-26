"""
    Script for parsing color information from Pokémon BD/SP ColorVariation.json files.
"""
# pylint: disable=import-error, wrong-import-position
import os
import sys
import argparse
from tkinter.filedialog import askopenfilenames

from bdsp_json import print_json_color_data

sys.path.append(os.path.join(os.path.dirname(__file__), "."))

from general import init_app


def main() -> int | str:
    """
    Program for parsing color information from Pokémon BD/SP ColorVariation.json files.
    :return: Status code or string.
    """
    init_app(os.path.join("images", "json_parser.tga"))
    parser = argparse.ArgumentParser(description="Parser for Pokémon BD/SP "
                                                 "ColorVariation.json files.")
    parser.add_argument("input_paths", nargs="*", type=str, default="",
                        help="Input JSON files")
    args = parser.parse_args()
    if len(args.input_paths) < 1:
        args.input_paths = askopenfilenames(title="Select JSON files",
                                            filetypes=[("JSON", "*.json")])
    for input_path in args.input_paths:
        print_json_color_data(input_path)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
