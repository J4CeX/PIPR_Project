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
    def __init__(self, mass, position, velocity):
        super().__init__(mass)
        self.positon = position
        self.velocity = velocity
