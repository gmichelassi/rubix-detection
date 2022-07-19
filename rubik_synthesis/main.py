from ursina import *
from rubik_synthesis.synthesis import build_rubik_cube

# de baixo pra cima sempre, da posição do observador
# da esq pra dir sempre, da posição do observador
rubik_colors = {
    'front': [color.red, color.red, color.orange, color.green, color.yellow, color.yellow, color.blue, color.white, color.white],
    'top': [color.green, color.orange, color.red, color.green, color.orange, color.white, color.green, color.green, color.green],
    'left': [color.white, color.blue, color.blue, color.yellow, color.green, color.orange, color.orange, color.blue, color.orange],
    'right': [color.blue, color.blue, color.blue, color.red, color.white, color.red, color.yellow, color.red, color.red],
    'back': [color.green, color.white, color.orange, color.green, color.blue, color.orange, color.yellow, color.yellow, color.yellow],
    'bottom': [color.yellow, color.yellow, color.red, color.orange, color.red, color.white, color.white, color.blue, color.white]
}


def run():
    cubes = build_rubik_cube(rubik_colors)


def main():
    app = Ursina()
    run()
    EditorCamera()
    app.run()
