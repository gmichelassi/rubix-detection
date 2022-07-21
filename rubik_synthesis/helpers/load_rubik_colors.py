import json

from .safety_check import safety_check


# Receives the file containing the relation between faces
# and its colors, loads it as a json and calls safety_check
# to confirm it is in the correct format
def load_rubik_colors(filename: str) -> dict:
    with open(filename) as jsonfile:
        rubik_colors = json.load(jsonfile)

    safety_check(rubik_colors)

    return rubik_colors
