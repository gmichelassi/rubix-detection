from rubik_synthesis.config import POSITIONS
from ursina import *


def build_base_cube(colors):
    parent = Entity(enabled=False)

    for i in range(3):
        direction = Vec3(0, 0, 0)
        direction[i] = 1
        current_color = colors[POSITIONS[i]]

        plane = Entity(parent=parent, model='plane', origin_y=-.5, texture='white_cube', color=current_color)
        plane.look_at(direction, 'up')

        mirror_plane = Entity(parent=parent, model='plane', origin_y=-.5, texture='white_cube', color=current_color)
        mirror_plane.look_at(-direction, 'up')

    parent.combine()

    return parent
