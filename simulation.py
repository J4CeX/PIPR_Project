import numpy as np
from objects import (
    OrbitalObject,
    CentralObject
)
from space import Space


class Simulation():
    def __init__(self, space: Space, central_object: CentralObject,
                 orbital_objects: OrbitalObject = []):
        self.space = space
        self.central_object = central_object
        self.orbital_objects = orbital_objects
        self.matrix = np.array(
            [[False for column in range(50)] for row in range(50)],
            dtype=bool
        )
