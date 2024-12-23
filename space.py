from PIL import (
    Image,
    ImageDraw
)
from objects import (
    OrbitalObject,
    CentralObject
)


class Space:
    def __init__(self, size: int, central_object: CentralObject,
                 orbital_objects: OrbitalObject = [], space_name='unknown'):
        self._size = size
        self._central_object = central_object
        self._orbital_objects = orbital_objects
        self.space_name = space_name

        # do nowej metody
        newSpace = Image.new('RGB', (size, size), (0, 0, 0))
        newSpace.save(f'{space_name}.jpg')
        with Image.open(f'{space_name}.jpg') as space:
            radius = central_object.diameter() / 2
            position = (size / 2, size / 2)
            draw = ImageDraw.Draw(space)
            draw.circle(position, radius, fill='white')
            space.save(f'{space_name}.jpg', quality=100)
            space.show()

    def size(self):
        return self._size
