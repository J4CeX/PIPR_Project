class Object:
    def __init__(self, mass, positionXY: tuple):
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
    def __init__(self, mass, diameter):
        super().__init__(mass, (0, 0))
        self._diameter = diameter

    def diameter(self):
        return self._diameter


class OrbitalObject(Object):
    def __init__(self, mass, positionXY, velocityXY: tuple):
        super().__init__(mass, positionXY)
        self.vx = velocityXY[0]
        self.vy = velocityXY[1]
