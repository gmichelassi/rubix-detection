import json

from .safety_check import safety_check


def load_rubik_colors(filename: str) -> dict:
    with open(filename) as jsonfile:
        rubik_colors = json.load(jsonfile)

    safety_check(rubik_colors)

    return rubik_colors
