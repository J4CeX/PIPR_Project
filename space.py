from objects import (
    OrbitalObject,
    CentralObject
)
from PIL import (
    Image,
    ImageDraw
)
from math import (
    sqrt
)


class Space:
    def __init__(self, size: int, scale: int, central_object: CentralObject,
                 orbital_objects: OrbitalObject = [], space_name='unknown'):
        space_image = Image.new('RGB', (size, size), (0, 0, 0))
        draw = ImageDraw.Draw(space_image)
        radius = central_object.diameter() / 2
        position = (size / 2, size / 2)
        central_object.set_position((0, 0))
        draw.circle(position, radius, fill='white')
        for object in orbital_objects:
            draw.point(position)
        self._space_name = space_name
        self._size = size
        self._scale = scale
        self.central_object = central_object
        self.orbital_objects = orbital_objects
        self._space_image = space_image
        self._draw = draw

    def simulate(self, steps: int):
        G = 1.2e-22
        M = self.central_object.mass()
        x1, y1 = self.central_object.position()
        for step in range(0, steps):
            for object in self.orbital_objects:
                x2, y2 = object.position()
                R = sqrt(pow(x2 - x1, 2)+pow(y2 - y1, 2))
                next_vx = object.velocity[0] - ((G * M) / pow(R, 3))
                next_vy = object.velocity[1] - ((G * M) / pow(R, 3))
                next_x = x2 + object.velocity[0]
                next_y = y2 + object.velocity[1]
                next_position = (next_x, next_y)
                object.velocity[0] = next_vx
                object.velocity[1] = next_vy
                object.set_position(next_position)

                x_draw, y_draw = object.position()
                x_draw += self.size()/2
                y_draw += self.size()/2
                self._draw.point((x_draw, y_draw))
        #         print((x2, y2), ' ', (x_draw, y_draw))
        # input()

    def show_image(self):
        self._space_image.show()

    def size(self):
        return self._size

    def scale(self):
        return self._scale

    def space_name(self):
        return self._space_name

    def info(self):
        info = ''
        info += f'Space name: {self._space_name}\n'
        info += f'Space Size: {self._size}\n'
        info += 'Central Object:\n'
        info += f'\tMass: {self.central_object.mass()}\n'
        info += f'\tDiameter: {self.central_object.diameter()}\n'
        info += 'Orbital Objects:\n'
        index = 1
        for object in self.orbital_objects:
            info += f'{index}.\tMass: {object.mass()}\n'
            info += f'\tPosition(x, y): {object.position()}\n'
            info += f'\tVelocity: {object.velocity}\n'
            index += 1
        return info
