from objects import (
    OrbitalObject,
    CentralObject,
    # ValueIsNotFloatError,
    # ValueIsNotIntegerError,
    # ValueIsNotPositiveError,
    # RGBValueError
)
from PIL import (
    Image,
    ImageDraw
)
from math import sqrt


class Space:
    """
    Class Space, Contains attributes:
    :param name: Space's name
    :type name: str

    :param size: Space's simulation image size
    :type size: positive integer

    :param scale: Space's simulation image scale
    :type scale: positive float

    :param central_object: Space's central object
    :type central_object: class CentralObject

    :param orbital_objects: Space's objects orbiting a central object
    :type orbital_objects: class OrbitalObject

    :param image: Space's class to generate simulation image
    :type image: class Image

    :param draw: Space's class to modify simulation image
    :type draw: class ImageDraw

    :param collisions: List of Space's collisions, location and time
    they occurred during the simulation
    :type collisions: list of tuple of scaled x and y (position) and integer
    """
    def __init__(self, size: int, scale: float, central_object: CentralObject,
                 orbital_objects: OrbitalObject = [],
                 name='unknown', collisions=[]):
        """
        Creates Space and create for it image of space with central object only
        basing on central object's diameter and scale of space image
        Gives class Space ability to change it image during simulation steps
        """
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
        """
        This Space's method simulate simulation of motion in a gravitational
        field basing on Space attributes data and given unit of time and its
        amount. Simulation places orbital object in position x=0 y=0 on
        a Cartesian plane and orbital objects on real position (real distance
        from central object). It calculate next position of orbital objects
        basing on their gravity acceleration vector (ax, ay), their velocity
        vector (vx, vy), their distance from central object, their previous
        position and central object's mass. After calculations it places all
        objects on generating image using scale and central object's position
        moved to center of the image (image size divided by 2) and convert
        result to integer to be able to place it in certain pixel. After
        simulation of one step, it checks if any collisions has occured.
        """
        collisions = []
        G = 6.67430e-11  # Gravitational constant
        T = time  # Unit of time
        M = self.central_object.mass()
        X, Y = self.central_object.position()
        SCALE = self.scale()
        objects = self.orbital_objects
        for step in range(steps):
            for object in objects:
                x, y = object.position()

                r = sqrt(x**2 + y**2)  # Distance from central to orbital obj.
                try:
                    a = -G * M / r**2  # Gravity acceleration
                    ax = a * (x / r)  # Grav. acc. vector horizontal component
                    ay = a * (y / r)  # Grav. acc. vector vertical component
                except ZeroDivisionError:
                    continue
                # Orbital object's next step values
                object.vx += ax * T  # Orbital obj. next vector hor. cmpt.
                object.vy += ay * T  # Orbital obj. next vector ver. cmpt.
                x += object.vx * T  # Orbital obj. next x position
                y += object.vy * T  # Orbital obj. next y position
                object.set_position((x, y))
                # Convert real positon to scaled for image
                x_pixel = int(X + x * SCALE)
                y_pixel = int(Y + y * SCALE)
                pixel = (x_pixel, y_pixel)
                object.set_pixel(pixel)
                self._draw.point(pixel, fill=object.color)
            # Searching for collisions in step
            quantity = len(self.orbital_objects)
            for first in range(quantity):
                f_pixel = objects[first].pixel()
                for second in range(first + 1, quantity):
                    s_pixel = objects[second].pixel()
                    if f_pixel == s_pixel:
                        self._draw.point(f_pixel, fill=(255, 200, 0))
                        collisions.append((f_pixel, step))
        self.collisions = collisions

    def info(self):
        """
        Method return informations about Space's attributes,
        last step of the simulation and collisions as string
        """
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
