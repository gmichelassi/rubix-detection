from .build_base_cube import build_base_cube
from ursina import *


def build_rubik_cube(rubik_colors):
    cubes = []

    for x in range(3):
        for y in range(3):
            for z in range(3):
                parent = build_parent(rubik_colors, x, y, z)

                cube = Entity(
                    model=copy(parent.model),
                    position=Vec3(x, y, z) - Vec3(1, 1, 1),
                    texture='white_cube',
                )

                cubes.append(cube)

    return cubes


def build_parent(rubik_colors, x: int, y: int, z: int):
    if x == 0 and y == 0 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][0],
            'left-right': rubik_colors['left'][2],
            'top-bottom': rubik_colors['bottom'][6]
        })
    elif x == 1 and y == 0 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][1],
            'left-right': color.black,
            'top-bottom': rubik_colors['bottom'][7]
        })
    elif x == 2 and y == 0 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][2],
            'left-right': rubik_colors['right'][0],
            'top-bottom': rubik_colors['bottom'][8]
        })
    elif x == 0 and y == 1 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][3],
            'left-right': rubik_colors['left'][5],
            'top-bottom': color.black
        })
    elif x == 1 and y == 1 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][4],
            'left-right': color.black,
            'top-bottom': color.black
        })
    elif x == 2 and y == 1 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][5],
            'left-right': rubik_colors['right'][3],
            'top-bottom': color.black
        })
    elif x == 0 and y == 2 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][6],
            'left-right': rubik_colors['left'][8],
            'top-bottom': rubik_colors['top'][0]
        })
    elif x == 1 and y == 2 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][7],
            'left-right': color.black,
            'top-bottom': rubik_colors['top'][1],
        })
    elif x == 2 and y == 2 and z == 0:
        parent = build_base_cube({
            'front-back': rubik_colors['front'][8],
            'left-right': rubik_colors['right'][6],
            'top-bottom': rubik_colors['top'][2]
        })

    elif x == 0 and y == 0 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': rubik_colors['left'][2],
            'top-bottom': rubik_colors['bottom'][3]
        })
    elif x == 1 and y == 0 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': color.black,
            'top-bottom': rubik_colors['bottom'][4]
        })
    elif x == 2 and y == 0 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': rubik_colors['right'][2],
            'top-bottom': rubik_colors['bottom'][5]
        })
    elif x == 0 and y == 1 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': rubik_colors['left'][4],
            'top-bottom': color.black
        })
    elif x == 1 and y == 1 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': color.black,
            'top-bottom': color.black
        })
    elif x == 2 and y == 1 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': rubik_colors['right'][4],
            'top-bottom': color.black
        })
    elif x == 0 and y == 2 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': rubik_colors['left'][7],
            'top-bottom': rubik_colors['top'][3]
        })
    elif x == 1 and y == 2 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': color.black,
            'top-bottom': rubik_colors['top'][4]
        })
    elif x == 2 and y == 2 and z == 1:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': rubik_colors['right'][7],
            'top-bottom': rubik_colors['top'][5]
        })

    elif x == 0 and y == 0 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][2],
            'left-right': rubik_colors['left'][0],
            'top-bottom': rubik_colors['bottom'][0]
        })
    elif x == 1 and y == 0 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][1],
            'left-right': color.black,
            'top-bottom': rubik_colors['bottom'][1]
        })
    elif x == 2 and y == 0 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][0],
            'left-right': rubik_colors['right'][2],
            'top-bottom': rubik_colors['bottom'][2]
        })
    elif x == 0 and y == 1 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][5],
            'left-right': rubik_colors['left'][3],
            'top-bottom': color.black
        })
    elif x == 1 and y == 1 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][4],
            'left-right': color.black,
            'top-bottom': color.black
        })
    elif x == 2 and y == 1 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][3],
            'left-right': rubik_colors['right'][5],
            'top-bottom': color.black
        })
    elif x == 0 and y == 2 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][8],
            'left-right': rubik_colors['left'][6],
            'top-bottom': rubik_colors['top'][6]
        })
    elif x == 1 and y == 2 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][7],
            'left-right': color.black,
            'top-bottom': rubik_colors['top'][7]
        })
    elif x == 2 and y == 2 and z == 2:
        parent = build_base_cube({
            'front-back': rubik_colors['back'][6],
            'left-right': rubik_colors['right'][8],
            'top-bottom': rubik_colors['top'][8]
        })
    else:
        parent = build_base_cube({
            'front-back': color.black,
            'left-right': color.black,
            'top-bottom': color.black
        })

    return parent
