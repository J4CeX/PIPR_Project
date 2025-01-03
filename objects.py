class Object:
    def __init__(self, mass: float, positionXY: tuple):
        self._mass = mass
        self.x = positionXY[0]
        self.y = positionXY[1]

    def mass(self):
        return self._mass

    def position(self):
        return (self.x, self.y)

    def set_position(self, xy: tuple):
        self.x = xy[0]
        self.y = xy[1]


class CentralObject(Object):
    def __init__(self, mass: float, diameter: float):
        super().__init__(mass, (0, 0))
        self._diameter = diameter

    def diameter(self):
        return self._diameter


class OrbitalObject(Object):
    def __init__(self, id: int, mass: float, positionXY: tuple,
                 velocityXY: tuple, color: tuple):
        super().__init__(mass, positionXY)
        if id < 0:
            raise ValueError('Id cannot be negative')
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
        self.x_pixel = new_pixel[0]
        self.y_pixel = new_pixel[1]
