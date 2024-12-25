from PIL import (
    Image,
    ImageDraw
)
from objects import (
    OrbitalObject,
    CentralObject
)


def print_central_object(space, space_image, draw):
    radius = space.central_object.diameter() / 2
    position = (space.size() / 2, space.size() / 2)
    draw.circle(position, radius, fill='white')


def print_orbital_objects(space, space_image, draw):
    for object in space.orbital_objects:
        draw.point(object.position)


class Space:
    def __init__(self, size: int, central_object: CentralObject,
                 orbital_objects: OrbitalObject = [], space_name='unknown'):
        self._space_name = space_name
        self._size = size
        self.central_object = central_object
        self.orbital_objects = orbital_objects

    def print(self):
        file_format = 'png'
        path = self.space_name()
        new_space = Image.new('RGB', (self.size(), self.size()), (0, 0, 0))
        new_space.save(f'{path}.{file_format}', f'{file_format}')
        with Image.open(f'{path}.{file_format}') as space_image:
            draw = ImageDraw.Draw(space_image)
            print_central_object(self, space_image, draw)
            print_orbital_objects(self, space_image, draw)
            space_image.save(f'{path}.{file_format}', f'{file_format}')
            space_image.show()

    def size(self):
        return self._size

    def space_name(self):
        return self._space_name
