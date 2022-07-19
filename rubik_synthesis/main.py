from ursina import *
from ursina import curve

from rubik_synthesis.synthesis import build_rubik_cube
from rubik_synthesis.helpers import load_rubik_colors


def run(rubik_colors: dict):
    cubes = build_rubik_cube(rubik_colors)

    rotation_helper = Entity()
    win_text_entity = Text(y=.35, text='', color=color.green, origin=(0, 0), scale=3)

    collider = Entity(model='cube', scale=3, collider='box', visible=False)

    def collider_input(key):
        if mouse.hovered_entity == collider:
            if key == 'left mouse down':
                rotate_side(mouse.normal, 1)
            elif key == 'right mouse down':
                rotate_side(mouse.normal, -1)

    collider.input = collider_input

    def reset_rotation_helper():
        [setattr(e, 'world_parent', scene) for e in cubes]
        rotation_helper.rotation = (0, 0, 0)

    def check_for_win():
        if {e.world_rotation for e in cubes} == {Vec3(0, 0, 0)}:
            win_text_entity.text = 'SOLVED!'
            win_text_entity.appear()
        else:
            win_text_entity.text = ''

    def rotate_side(normal, direction=1, speed=1):
        if normal == Vec3(1, 0, 0):
            [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.x > 0]
            rotation_helper.animate('rotation_x', 90 * direction, duration=.2 * speed, curve=curve.linear)
        elif normal == Vec3(-1, 0, 0):
            [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.x < 0]
            rotation_helper.animate('rotation_x', -90 * direction, duration=.2 * speed, curve=curve.linear)

        elif normal == Vec3(0, 1, 0):
            [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.y > 0]
            rotation_helper.animate('rotation_y', 90 * direction, duration=.2 * speed, curve=curve.linear)
        elif normal == Vec3(0, -1, 0):
            [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.y < 0]
            rotation_helper.animate('rotation_y', -90 * direction, duration=.2 * speed, curve=curve.linear)

        elif normal == Vec3(0, 0, 1):
            [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.z > 0]
            rotation_helper.animate('rotation_z', -90 * direction, duration=.2 * speed, curve=curve.linear)
        elif normal == Vec3(0, 0, -1):
            [setattr(e, 'world_parent', rotation_helper) for e in cubes if e.z < 0]
            rotation_helper.animate('rotation_z', 90 * direction, duration=.2 * speed, curve=curve.linear)

        invoke(reset_rotation_helper, delay=.22 * speed)

        if speed:
            collider.ignore_input = True
            invoke(setattr, collider, 'ignore_input', False, delay=.24 * speed)
            invoke(check_for_win, delay=.25 * speed)


def main():
    rubik_colors = load_rubik_colors('./rubik_synthesis/input/first_example.json')

    app = Ursina()
    run(rubik_colors)
    EditorCamera()
    app.run()
