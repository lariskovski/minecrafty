from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
punch_sound = Audio('assets/punch_sound',loop = False, autoplay = False)

textures = [grass_texture, stone_texture, brick_texture, dirt_texture]

block_pick = 1


class Voxel(Button):


    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5)


    def input(self,key):
        if self.hovered:

            if key == 'left mouse down':
                try:
                    punch_sound.play()
                    voxel = Voxel(position = self.position + mouse.normal, texture = textures[block_pick-1])
                except IndexError:
                    pass

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )


# Generate floor
floor_block_size = 5
# Forward and backwards
for z in range(floor_block_size):
    # Left and right
    for x in range(floor_block_size):
        volex = Voxel(position = (x, 0, z))


player = FirstPersonController()
sky = Sky()

z_min_edge = 0
z_max_edge = floor_block_size - 1

# This is called at every frame
def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

    # Add infinite border to side
    global z_min_edge, z_max_edge, floor_block_size
    print(player.position.x, player.position.z)
    if int(player.position.z) == z_min_edge:
        for x in range(0, floor_block_size):
            volex = Voxel(position = (x, 0, z_min_edge - 1))
        z_min_edge-=1
        z_max_edge-=1

if __name__ == "__main__":
    app.run()
