from ursina import *
from ursina import curve

from rubik_synthesis.synthesis import build_rubik_cube
from rubik_synthesis.helpers import load_rubik_colors


def run(rubik_colors: dict):
    window.color = color.black
    cubes = build_rubik_cube(rubik_colors)

    # Defines the collider, which will be used to identify the user
    # interaction with the cube
    collider = Entity(model='cube', scale=3, collider='box', visible=False)

    # Defines the direction of rotation based on the user input
    def collider_input(key):
        if mouse.hovered_entity == collider:
            if key == 'left mouse down':
                rotate_side(mouse.normal, 1)
            elif key == 'right mouse down':
                rotate_side(mouse.normal, -1)

    collider.input = collider_input

    # Entity that will be used to recalculate the cubes
    # positions on request for rotation
    rotation_helper = Entity()

    # Resets the cubes positions to match the scene after the animation end.
    def reset_rotation():
        for cube in cubes:
            position, rotation = round(cube.world_position, 1), cube.world_rotation
            cube.parent = scene
            cube.position, cube.rotation = position, rotation

        rotation_helper.rotation = 0

    # Function that executes the animation of rotation. It uses the rotation_helper entity
    # to calculate the new positions. We use the normal and direction to define the face that
    # was clicked, then knowing which cubes to rotate.
    def rotate_side(normal, direction):
        if normal == Vec3(1, 0, 0):
            for cube in cubes:
                if cube.x > 0:
                    cube.parent = rotation_helper
            rotation_helper.animate('rotation_x', 90 * direction, duration=.2, curve=curve.linear)
        elif normal == Vec3(-1, 0, 0):
            for cube in cubes:
                if cube.x < 0:
                    cube.parent = rotation_helper
            rotation_helper.animate('rotation_x', -90 * direction, duration=.2, curve=curve.linear)

        elif normal == Vec3(0, 1, 0):
            for cube in cubes:
                if cube.y > 0:
                    cube.parent = rotation_helper
            rotation_helper.animate('rotation_y', 90 * direction, duration=.2, curve=curve.linear)
        elif normal == Vec3(0, -1, 0):
            for cube in cubes:
                if cube.y < 0:
                    cube.parent = rotation_helper
            rotation_helper.animate('rotation_y', -90 * direction, duration=.2, curve=curve.linear)

        elif normal == Vec3(0, 0, 1):
            for cube in cubes:
                if cube.z > 0:
                    cube.parent = rotation_helper
            rotation_helper.animate('rotation_z', -90 * direction, duration=.2, curve=curve.linear)
        elif normal == Vec3(0, 0, -1):
            for cube in cubes:
                if cube.z < 0:
                    cube.parent = rotation_helper
            rotation_helper.animate('rotation_z', 90 * direction, duration=.2, curve=curve.linear)

        invoke(reset_rotation, delay=.22)

        # Unable the possibility of user interaction while the animation is
        # being executed, to prevent bugs.
        collider.ignore_input = True
        invoke(setattr, collider, 'ignore_input', False, delay=.24)


# Main function, it loads the file containing the colors,
# initializes and runs the game
def main():
    rubik_colors = load_rubik_colors('./rubik_synthesis/input/first_example.json')

    app = Ursina()
    run(rubik_colors)
    EditorCamera()
    app.run()
