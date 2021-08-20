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


# Forward and backwards
for z in range(8):
    # Left and right
    for x in range(8):
        volex = Voxel(position = (z, 0, x))


if __name__ == '__main__':
    app = Ursina()
    player = FirstPersonController()
    app.run()
