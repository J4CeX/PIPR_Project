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
                 orbital_objects: OrbitalObject = [], spaceName='unknown'):
        self._size = size
        self._central_object = central_object
        self._orbital_objects = orbital_objects
        self.spaceName = spaceName

        newSpace = Image.new('RGB', (size, size), (0, 0, 0))
        newSpace.save(f'{spaceName}.png', 'PNG')
        with Image.open(f'{spaceName}.png') as space:
            diameter = central_object.diameter()
            position = (size / 2, size / 2)
            draw = ImageDraw.Draw(space)
            draw.circle(position, diameter, 'white')
            space.save(f'{spaceName}.png', 'PNG')
            space.show()

    def size(self):
        return self._size
