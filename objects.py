from errors import (
    ValueIsNotFloatError,
    ValueIsNotIntegerError,
    ValueIsNotPositiveError,
    RGBValueError
)


class Object:
    """
    Class Object, Contains attributes:
    :param mass: object's mass
    :type mass: positive float

    :param x and y: object's position
    :type x and y: float tuple
    """
    def __init__(self, mass: float, positionXY: tuple):
        if type(mass) is not float:
            raise ValueIsNotFloatError(mass)
        if mass <= 0:
            raise ValueIsNotPositiveError(mass)
        if type(positionXY[0]) is not float:
            raise ValueIsNotFloatError(positionXY[0])
        if type(positionXY[1]) is not float:
            raise ValueIsNotFloatError(positionXY[1])

        self._mass = mass
        self.x = positionXY[0]
        self.y = positionXY[1]

    def mass(self):
        return self._mass

    def position(self):
        return (self.x, self.y)

    def set_position(self, xy: tuple):
        if type(xy[0]) is not float:
            raise ValueIsNotFloatError(xy[0])
        if type(xy[1]) is not float:
            raise ValueIsNotFloatError(xy[1])
        self.x = xy[0]
        self.y = xy[1]


class CentralObject(Object):
    """
    Class CentralObject, inherits from class Object
    Contains attributes:
    :param mass: central object's mass
    :type mass: positive float

    :param x and y: central object's position
    :type x and y: tuple of floats

    :param diameter: central object's diameter
    :type diameter: positive float
    """
    def __init__(self, mass: float, diameter: float):
        super().__init__(mass, (0.0, 0.0))
        if type(diameter) is not float:
            raise ValueIsNotFloatError(diameter)
        if diameter <= 0:
            raise ValueIsNotPositiveError(diameter)

        self._diameter = diameter

    def diameter(self):
        return self._diameter


class OrbitalObject(Object):
    """
    Class OrbitalObject, inherits from class Object
    Contains attributes:
    :param id: orbital object's id
    :type id: positive integer

    :param mass: orbital object's mass
    :type mass: float

    :param x and y: orbital object's position
    :type x and y: tuple of floats

    :param vx and vy: orbital object's velocity vector values
    :type vx and xy: float

    :param x_pixel and y_pixel: orbital object's position in simulation image
    :type x_pixel and y_pixel: int

    :param color: orbital object's color in simulation image
    :type color: tuple of integers in the range 0 to 255
    """
    def __init__(self, id: int, mass: float, positionXY: tuple,
                 velocityXY: tuple, color: tuple):
        super().__init__(mass, positionXY)
        if type(id) is not int:
            raise ValueIsNotIntegerError(id)
        if id <= 0:
            raise ValueIsNotPositiveError(id)
        if type(velocityXY[0]) is not float:
            raise ValueIsNotFloatError(velocityXY[0])
        if type(velocityXY[1]) is not float:
            raise ValueIsNotFloatError(velocityXY[1])
        if type(color[0]) is not int:
            raise ValueIsNotIntegerError(color[0])
        if type(color[1]) is not int:
            raise ValueIsNotIntegerError(color[1])
        if type(color[2]) is not int:
            raise ValueIsNotIntegerError(color[2])
        if color[0] < 0 or color[0] > 255:
            raise RGBValueError(color[0])
        if color[1] < 0 or color[1] > 255:
            raise RGBValueError(color[1])
        if color[2] < 0 or color[2] > 255:
            raise RGBValueError(color[2])

        self._id = id
        self.vx = velocityXY[0]
        self.vy = velocityXY[1]
        self.x_pixel = None
        self.y_pixel = None
        self.color = color

    def id(self):
        return self._id

    def velocity(self):
        return (self.vx, self.vy)

    def pixel(self):
        return (self.x_pixel, self.y_pixel)

    def set_pixel(self, new_pixel: tuple):
        if type(new_pixel[0]) is not int:
            raise ValueIsNotIntegerError(new_pixel[0])
        if type(new_pixel[1]) is not int:
            raise ValueIsNotIntegerError(new_pixel[1])
        self.x_pixel = new_pixel[0]
        self.y_pixel = new_pixel[1]
