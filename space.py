# from PIL import (
#     Image,
#     ImageDraw
# )
from objects import (
    OrbitalObject,
    CentralObject
)


class Space:
    def __init__(self, size: int, central_object: CentralObject,
                 orbital_objects: OrbitalObject = [], space_name='unknown'):
        self._space_name = space_name
        self._size = size
        self.central_object = central_object
        self.orbital_objects = orbital_objects

    def print(self):
        pass
        # path = f'simulations/{self.space_name()}.png'
        # space_image = Image.new('RGB', (self.size(), self.size()), (0, 0, 0))
        # draw = ImageDraw.Draw(space_image)
        # radius = self.central_object.diameter() / 2
        # position = (self.size() / 2, self.size() / 2)
        # draw.circle(position, radius, fill='white')
        # for object in self.orbital_objects:
        #     draw.point(object.position)
        # space_image.save(path)
        # space_image.show()

    def open(self):
        pass

    def save(self):
        pass

    def size(self):
        return self._size

    def space_name(self):
        return self._space_name
