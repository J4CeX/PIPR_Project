from objects import (
    OrbitalObject,
    CentralObject
)
from PIL import (
    Image,
    ImageDraw
)


class Space:
    def __init__(self, size: int, central_object: CentralObject,
                 orbital_objects: OrbitalObject = [], space_name='unknown'):
        space_image = Image.new('RGB', (size, size), (0, 0, 0))
        draw = ImageDraw.Draw(space_image)
        radius = central_object.diameter() / 2
        position = (size / 2, size / 2)
        draw.circle(position, radius, fill='white')
        for object in orbital_objects:
            draw.point(object.position())
        self._space_name = space_name
        self._size = size
        self.central_object = central_object
        self.orbital_objects = orbital_objects
        self._space_image = space_image
        self._draw = draw

    def simulate(self, steps: int):
        for step in range(0, steps):
            for object in self.orbital_objects:
                object.x += object.velocity
                self._draw.point(object.position())

    def show(self):
        self._space_image.show()

    def size(self):
        return self._size

    def space_name(self):
        return self._space_name
