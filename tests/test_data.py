from data import (
    load_data,
    save_data
)
from objects import (
    CentralObject,
    OrbitalObject
)
from space import Space


def test_load_data():
    path = 'simulations/test/test.json'
    with open(path, 'r') as file_handle:
        space = load_data(file_handle)
        assert space.size() == 200
        assert space.scale() == 200
        assert space.space_name() == 'test'
        assert space.central_object.mass() == 2000
        assert space.central_object.diameter() == 100
        assert space.orbital_objects[0].mass() == 200
        assert space.orbital_objects[0].position() == (2, 2)
        assert space.orbital_objects[0].velocity() == (20, 0)
        assert space.orbital_objects[1].mass() == 100
        assert space.orbital_objects[1].position() == (10, 5)
        assert space.orbital_objects[1].velocity() == (20, 0)


def test_save_data():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), (20, 0)),
        OrbitalObject(100, (10, 5), (20, 0))
    ]
    space = Space(200, 200, central_object, orbital_objects, 'test')
    save_data(space)
