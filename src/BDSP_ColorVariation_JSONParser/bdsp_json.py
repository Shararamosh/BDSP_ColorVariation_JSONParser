"""
    Script containing functions to deal with JSON files from Pokémon BD/SP games.
"""
# pylint: disable=import-error, wrong-import-position
import os
import sys
import json
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), "."))

from general import RICH_CONSOLE


def print_json_color_data(file_path: str):
    """
    Prints out information from ColorVariation.json file originating from Pokémon BD/SP games.
    :param file_path: Path to JSON file.
    """
    if not os.path.exists(file_path):
        logging.warning("Path %s does not exist.", file_path)
        return
    if not os.path.isfile(file_path):
        logging.warning("Path %s is not a file.", file_path)
        return
    if not file_path.lower().endswith(".json"):
        logging.warning("Path %s is not a JSON file.", file_path)
        return
    with open(file_path, encoding="utf-8") as json_file:
        RICH_CONSOLE.print(f"{file_path}:")
        json_data = json.load(json_file)
        k = 0
        s = "00"
        while "Property" + s in json_data:
            property_data = json_data["Property" + s][0]
            RICH_CONSOLE.print(f"Property {s}:")
            colors_data = property_data["colors"]
            current_material_index = -1
            for color_data in colors_data:
                if color_data is not None:
                    c = color_data["channel"]
                    if color_data["materialIndex"] > current_material_index:
                        current_material_index = color_data["materialIndex"]
                        RICH_CONSOLE.print(f"Material Index: {current_material_index}.")
                    color_dict = color_data["color"]
                    if color_dict is not None:
                        RICH_CONSOLE.print(f"[{c:d}]: {get_color_dict_str(color_dict)}.")
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
