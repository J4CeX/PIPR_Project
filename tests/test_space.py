from simulation import Space
from objects import OrbitalObject, CentralObject


def test_Space_create():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, 1, 2),
        OrbitalObject(100, 2, 2)
    ]
    space = Space(500, central_object, orbital_objects)
    assert space.size() == 500
    assert space._central_object.diameter() == 100
    assert space._central_object.mass() == 2000
    assert space._orbital_objects[0].mass() == 200
    assert space._orbital_objects[1].mass() == 100
