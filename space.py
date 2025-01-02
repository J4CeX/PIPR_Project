from objects import (
    OrbitalObject,
    CentralObject
)
from PIL import (
    Image,
    ImageDraw
)
from math import sqrt


class Space:
    def __init__(self, size: int, scale: int, central_object: CentralObject,
                 orbital_objects: OrbitalObject = [],
                 name='unknown', collisions=[]):
        space_image = Image.new('RGB', (size, size), (0, 0, 0))
        draw = ImageDraw.Draw(space_image)
        radius = (central_object.diameter() / 2) * scale
        position = (size / 2, size / 2)
        central_object.set_position(position)
        draw.circle(position, radius, fill='white')
        self._name = name
        self._size = size
        self._scale = scale
        self.central_object = central_object
        self.orbital_objects = orbital_objects
        self._image = space_image
        self._draw = draw
        self.collisions = collisions

    def show_image(self):
        self._image.show()

    def size(self):
        return self._size

    def scale(self):
        return self._scale

    def name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def set_size(self, new_size):
        self._size = new_size

    def set_scale(self, new_scale):
        self._scale = new_scale

    def simulate(self, steps: int, time: int):
        collisions = []
        G = 6.67430e-11
        T = time
        M = self.central_object.mass()
        X, Y = self.central_object.position()
        SCALE = self.scale()
        objects = self.orbital_objects
        for step in range(steps):
            for object in objects:
                x, y = object.position()

                r = sqrt(x**2 + y**2)
                a = -G * M / r**2
                ax = a * (x / r)
                ay = a * (y / r)

                object.vx += ax * T
                object.vy += ay * T
                x += object.vx * T
                y += object.vy * T
                object.set_position((x, y))

                x_pixel = int(X + x * SCALE)
                y_pixel = int(Y + y * SCALE)
                pixel = (x_pixel, y_pixel)
                object.set_pixel(pixel)
                self._draw.point(pixel, fill=object.color)
            quantity = len(self.orbital_objects)
            for first in range(quantity):
                for second in range(first + 1, quantity):
                    if objects[first].pixel() == objects[second].pixel():
                        self._draw.point(pixel, fill='yellow')
                        collisions.append((objects[first].pixel(), step))
        self.collisions = collisions

    def info(self):
        info = ''
        info += f'Space name: {self._name}\n'
        info += f'Space size(px): {self._size}\n'
        info += f'Space scale(px/m): {self._scale}\n'
        info += 'Central Object:\n'
        info += f'\tMass(kg): {self.central_object.mass()}\n'
        info += f'\tDiameter(m): {self.central_object.diameter()}\n'
        info += 'Orbital Objects:\n'
        index = 1
        for object in self.orbital_objects:
            info += f'Id: {object.id()}\n'
            info += f'\tMass(kg): {object.mass()}\n'
            info += f'\tPosition(x, y): {object.position()}\n'
            info += f'\tVelocity(x, y): {object.velocity()}\n'
            info += f'\tColor: {object.color}\n'
            index += 1
        info += f'Collisions: {len(self.collisions)}\n'
        index = 1
        for collision in self.collisions:
            info += f'{index}.:\t'
            info += f'Position(x, y): {collision[0]}; '
            info += f'Step: {collision[1]}\n'
            index += 1
        return info
