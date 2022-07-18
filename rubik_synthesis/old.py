from ursina import *


class Game(Ursina):
    def __init__(self):
        super().__init__()
        window.fullscreen = True
        window.color = color.black

        EditorCamera()

        pivot = Entity()
        DirectionalLight(parent=pivot, x=2, y=2, z=3, shadows=True, rotation=(45, -45, 45))
        AmbientLight(color=color.rgba(100, 100, 100, 0.000001))

        self.load_game()

    def load_game(self):
        self.PARENT = Entity()

        self.configure_cube_positions()
        self.CUBES = [
            Entity(model='models/cube', texture='textures/rubik_texture', position=pos) for pos in self.SIDE_POSITIONS
        ]

        self.rotation_axes = {'LEFT': 'x', 'RIGHT': 'x', 'TOP': 'y', 'BOTTOM': 'y', 'FACE': 'z', 'BACK': 'z'}
        self.cubes_side_positions = {'LEFT': self.LEFT, 'BOTTOM': self.BOTTOM, 'RIGHT': self.RIGHT, 'FACE': self.FACE,
                                    'BACK': self.BACK, 'TOP': self.TOP}

        self.animation_duration = 0.5
        self.allow_player_action = True
        self.game_mode_on = False
        self.message = Text(text="To start the game, press G", origin=(0, 19), color=color.white)

        self.create_sensors()

    def configure_cube_positions(self):
        self.LEFT = {Vec3(-1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
        self.BOTTOM = {Vec3(x, -1, z) for x in range(-1, 2) for z in range(-1, 2)}
        self.FACE = {Vec3(x, y, -1) for x in range(-1, 2) for y in range(-1, 2)}
        self.BACK = {Vec3(x, y, 1) for x in range(-1, 2) for y in range(-1, 2)}
        self.RIGHT = {Vec3(1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
        self.TOP = {Vec3(x, 1, z) for x in range(-1, 2) for z in range(-1, 2)}
        self.SIDE_POSITIONS = self.LEFT | self.BOTTOM | self.FACE | self.BACK | self.RIGHT | self.TOP

    def create_sensors(self):
        sensor = lambda name, pos, scale: Entity(name=name, position=pos, model='cube', color=color.dark_gray,
                                                        scale=scale, collider='box', visible=False)
        self.LEFT_sensor = sensor(name='LEFT', pos=(-0.99, 0, 0), scale=(1.01, 3.01, 3.01))
        self.FACE_sensor = sensor(name='FACE', pos=(0, 0, -0.99), scale=(3.01, 3.01, 1.01))
        self.BACK_sensor = sensor(name='BACK', pos=(0, 0, 0.99), scale=(3.01, 3.01, 1.01))
        self.RIGHT_sensor = sensor(name='RIGHT', pos=(0.99, 0, 0), scale=(1.01, 3.01, 3.01))
        self.TOP_sensor = sensor(name='TOP', pos=(0, 1, 0), scale=(3.01, 1.01, 3.01))
        self.BOTTOM_sensor = sensor(name='BOTTOM', pos=(0, -1, 0), scale=(3.01, 1.01, 3.01))

    def input(self, key):
        if key in 'mouse1 mouse3' and self.game_mode_on and self.allow_player_action:
            for collision in mouse.collisions:
                collider_position = collision.entity.name
                if (key == 'mouse1' and collider_position in 'LEFT RIGHT FACE BACK' or
                        key == 'mouse3' and collider_position in 'TOP BOTTOM'):
                    self.rotate_side(collider_position)
                    break
        if key == 'g':
            self.toggle_game_mode()

        super().input(key)

    def toggle_game_mode(self):
        self.game_mode_on = not self.game_mode_on
        msg = dedent(f"{'GAME mode ON' if self.game_mode_on else 'VIEW mode ON'}"
                     f" (to switch - press G)").strip()
        self.message.text = msg

    def rotate_side(self, side_name):
        self.allow_player_action = False
        cube_positions = self.cubes_side_positions[side_name]
        rotation_axis = self.rotation_axes[side_name]
        self.recalculate_position_and_rotation()
        for cube in self.CUBES:
            if cube.position in cube_positions:
                cube.parent = self.PARENT
                eval(f'self.PARENT.animate_rotation_{rotation_axis}(90, duration=self.animation_duration)')
        invoke(self.toggle_animation_trigger, delay=self.animation_duration + 0.11)

    def recalculate_position_and_rotation(self):
        for cube in self.CUBES:
            if cube.parent == self.PARENT:
                world_pos, world_rot = round(cube.world_position, 1), cube.world_rotation
                cube.parent = scene
                cube.position, cube.rotation = world_pos, world_rot
        self.PARENT.rotation = 0

    def toggle_animation_trigger(self):
        self.allow_player_action = not self.allow_player_action


if __name__ == '__main__':
    game = Game()
    game.run()
