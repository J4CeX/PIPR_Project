import numpy as np
from space import Space
from PIL import (
    Image,
    ImageDraw
)


class Simulation():
    def __init__(self, space: Space):
        size = space.size()
        space_image = Image.new('RGB', (size, size), (0, 0, 0))
        draw = ImageDraw.Draw(space_image)
        radius = space.central_object.diameter() / 2
        position = (size / 2, size / 2)
        draw.circle(position, radius, fill='white')
        for object in space.orbital_objects:
            draw.point(object.position)
        self.space = space
        self.space_image = space_image

    def simulate(self):
        self.space_image.show()

    def save(self):
        path = f'simulations/{self.space.space_name()}.png'
        self.space_image.save(path)
