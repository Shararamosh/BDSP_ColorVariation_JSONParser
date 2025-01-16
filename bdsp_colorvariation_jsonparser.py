"""
    Script for parsing color information from Pokémon BD/SP ColorVariation.json files.
"""
import os
import sys
import json
import argparse


def print_json_color_data(file_path: str):
    """
    Prints out information from ColorVariation.json file originating from Pokémon BD/SP games.
    :param file_path: Path to JSON file.
    """
    if not os.path.exists(file_path):
        print("Path does not exist.")
        return
    if not os.path.isfile(file_path):
        print("Path is not a file.")
        return
    if not file_path.lower().endswith(".json"):
        print("Path is not a JSON file.")
        return
    with open(file_path, encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        k = 0
        s = "00"
        while "Property" + s in json_data:
            property_data = json_data["Property" + s][0]
            print("Property" + s + ":")
            colors_data = property_data["colors"]
            current_material_index = -1
            for color_data in colors_data:
                if color_data is not None:
                    c = color_data["channel"]
                    if color_data["materialIndex"] > current_material_index:
                        current_material_index = color_data["materialIndex"]
                        print("Material Index: " + str(current_material_index) + ".")
                    color_dict = color_data["color"]
                    if color_dict is not None:
                        color_dict_str = get_color_dict_str(color_dict)
                        print(f"[{c:d}]: {color_dict_str}.")
            k = k + 1
            if k < 10:
                s = "0" + str(k)
            else:
                s = str(k)


def get_color_dict_str(color_dict: dict) -> str:
    """
    Converts color dict to printable string.
    :param color_dict: Color dict (R, G, B, A).
    :return: String.
    """
    r = color_dict["r"]
    g = color_dict["g"]
    b = color_dict["b"]
    a = color_dict["a"]
    lc = f"({r:.8f}, {g:.8f}, {b:.8f}, {a:.8f})"
    hc = format(round(float(color_dict["r"]) * 255.0), "x").upper()
    hc = hc + format(round(float(color_dict["g"]) * 255.0), "x").upper()
    hc = hc + format(round(float(color_dict["b"]) * 255.0), "x").upper()
    return f"{lc} -> {hc}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="BD/SP ColorVariation Parser",
                                     description="Parser for Pokémon BD/SP "
                                                 "ColorVariation.json files.")
    parser.add_argument("input_paths", nargs="*", type=str, default="",
                        help="Input JSON files")
    args = parser.parse_args()
    if len(args.input_paths) < 1:
        input_path = input("JSON file path: ")
        print_json_color_data(input_path)
    else:
        for input_path in args.input_paths:
            print(f"{input_path}:")
            print_json_color_data(input_path)
    sys.exit(os.EX_OK)
