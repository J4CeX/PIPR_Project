from space import Space
from objects import OrbitalObject, CentralObject


def test_Space_create():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), 2),
        OrbitalObject(100, (10, 5), 2)
    ]
    space = Space(500, central_object, orbital_objects)
    assert space.size() == 500
    assert space.central_object.diameter() == 100
    assert space.central_object.mass() == 2000
    assert space.orbital_objects[0].mass() == 200
    assert space.orbital_objects[1].mass() == 100


def test_Space_simulate():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), 2),
        OrbitalObject(100, (10, 5), 2)
    ]
    space = Space(200, central_object, orbital_objects, 'test')
    space.simulate(1)


def test_Space_save():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), 2),
        OrbitalObject(100, (10, 5), 2)
    ]
    space = Space(500, central_object, orbital_objects, 'test')
    space.save()
