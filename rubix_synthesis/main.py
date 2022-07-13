from ursina import *
from ursina.shaders import lit_with_shadows_shader


class Game(Ursina):
    def __init__(self):
        super().__init__()
        window.fullscreen = True

        Entity(model='quad', scale=60, texture='white_cube', texture_scale=(60, 60),
               rotation_x=90, y=-5, color=color.light_gray, shader=lit_with_shadows_shader)
        Entity(model='sphere', scale=100, texture='textures/background', double_sided=True)
        Entity(model='plane', scale=100, texture='textures/background', position=(0, -3, 0))

        EditorCamera()
        camera.world_position = (0, 0, -15)

        pivot = Entity()
        DirectionalLight(parent=pivot, x=2, y=2, z=3, shadows=True, rotation=(45, -45, 45))
        AmbientLight(color=color.rgba(100, 100, 100, 0.000001))

        self.model, self.texture = 'models/cube', 'textures/rubik_texture'
        self.load_game()

    def load_game(self):
        self.create_cube_positions()
        self.CUBES = [Entity(model=self.model, texture=self.texture, position=pos) for pos in self.SIDE_POSITIONS]
        self.PARENT = Entity()
        self.rotation_axes = {'LEFT': 'x', 'RIGHT': 'x', 'TOP': 'y', 'BOTTOM': 'y', 'FACE': 'z', 'BACK': 'z'}
        self.cubes_side_positons = {'LEFT': self.LEFT, 'BOTTOM': self.BOTTOM, 'RIGHT': self.RIGHT, 'FACE': self.FACE,
                                    'BACK': self.BACK, 'TOP': self.TOP}
        self.animation_time = 0.5
        self.action_trigger = True
        self.action_mode = True
        self.message = Text(origin=(0, 19), color=color.white)
        self.toggle_game_mode()
        self.create_sensors()

    def create_sensors(self):
        create_sensor = lambda name, pos, scale: Entity(name=name, position=pos, model='cube', color=color.dark_gray,
                                                        scale=scale, collider='box', visible=False)
        self.LEFT_sensor = create_sensor(name='LEFT', pos=(-0.99, 0, 0), scale=(1.01, 3.01, 3.01))
        self.FACE_sensor = create_sensor(name='FACE', pos=(0, 0, -0.99), scale=(3.01, 3.01, 1.01))
        self.BACK_sensor = create_sensor(name='BACK', pos=(0, 0, 0.99), scale=(3.01, 3.01, 1.01))
        self.RIGHT_sensor = create_sensor(name='RIGHT', pos=(0.99, 0, 0), scale=(1.01, 3.01, 3.01))
        self.TOP_sensor = create_sensor(name='TOP', pos=(0, 1, 0), scale=(3.01, 1.01, 3.01))
        self.BOTTOM_sensor = create_sensor(name='BOTTOM', pos=(0, -1, 0), scale=(3.01, 1.01, 3.01))

    def toggle_game_mode(self):
        self.action_mode = not self.action_mode
        msg = dedent(f"{'GAME mode ON' if self.action_mode else 'VIEW mode ON'}"
                     f" (to switch - press G)").strip()
        self.message.text = msg

    def toggle_animation_trigger(self):
        self.action_trigger = not self.action_trigger

    def rotate_side(self, side_name):
        self.action_trigger = False
        cube_positions = self.cubes_side_positons[side_name]
        rotation_axis = self.rotation_axes[side_name]
        self.reparent_to_scene()
        for cube in self.CUBES:
            if cube.position in cube_positions:
                cube.parent = self.PARENT
                eval(f'self.PARENT.animate_rotation_{rotation_axis}(90, duration=self.animation_time)')
        invoke(self.toggle_animation_trigger, delay=self.animation_time + 0.11)

    def reparent_to_scene(self):
        for cube in self.CUBES:
            if cube.parent == self.PARENT:
                world_pos, world_rot = round(cube.world_position, 1), cube.world_rotation
                cube.parent = scene
                cube.position, cube.rotation = world_pos, world_rot
        self.PARENT.rotation = 0

    def create_cube_positions(self):
        self.LEFT = {Vec3(-1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
        self.BOTTOM = {Vec3(x, -1, z) for x in range(-1, 2) for z in range(-1, 2)}
        self.FACE = {Vec3(x, y, -1) for x in range(-1, 2) for y in range(-1, 2)}
        self.BACK = {Vec3(x, y, 1) for x in range(-1, 2) for y in range(-1, 2)}
        self.RIGHT = {Vec3(1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
        self.TOP = {Vec3(x, 1, z) for x in range(-1, 2) for z in range(-1, 2)}
        self.SIDE_POSITIONS = self.LEFT | self.BOTTOM | self.FACE | self.BACK | self.RIGHT | self.TOP

    def input(self, key):
        if key in 'mouse1 mouse3' and self.action_mode and self.action_trigger:
            for hitinfo in mouse.collisions:
                collider_name = hitinfo.entity.name
                if (key == 'mouse1' and collider_name in 'LEFT RIGHT FACE BACK' or
                        key == 'mouse3' and collider_name in 'TOP BOTTOM'):
                    self.rotate_side(collider_name)
                    break
        if key == 'g':
            self.toggle_game_mode()
        super().input(key)


if __name__ == '__main__':
    game = Game()
    game.run()
