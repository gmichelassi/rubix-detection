from ursina import *

from rubik_synthesis.synthesis import build_rubik_cube
from rubik_synthesis.helpers import load_rubik_colors


def run(rubik_colors: dict):
    cubes = build_rubik_cube(rubik_colors)


def main():
    rubik_colors = load_rubik_colors('./rubik_synthesis/input/first_example.json')

    app = Ursina()
    run(rubik_colors)
    EditorCamera()
    app.run()
