from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# This is called at every frame
def update():
    pass

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.white,
            highlight_color = color.lime
        )
    
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            
            if key == 'right mouse down':
                destroy(self)


app = Ursina()


floor_block_size = 20
# Forward and backwards
for z in range(floor_block_size):
    # Left and right
    for x in range(floor_block_size):
        volex = Voxel(position = (x, 0, z))


player = FirstPersonController()

app.run()
