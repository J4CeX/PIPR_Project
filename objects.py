class Object:
    def __init__(self, mass):
        self._mass = mass

    def mass(self):
        return self._mass


class CentralObject(Object):
    def __init__(self, mass, diameter):
        super().__init__(mass)
        self._diameter = diameter

    def diameter(self):
        return self._diameter


class OrbitalObject(Object):
    def __init__(self, mass, positionXY: tuple, velocity):
        super().__init__(mass)
        self.x = positionXY[0]
        self.y = positionXY[1]
        self.velocity = velocity

    def position(self):
        return (self.x, self.y)
