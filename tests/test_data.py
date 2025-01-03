from data import (
    load_data,
    save_data
)
from objects import (
    CentralObject,
    OrbitalObject
)
from space import Space
import os


def test_load_and_save_data(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: '')
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(1, 200, (2, 2), (20, 0), (255, 0, 0)),
        OrbitalObject(2, 100, (10, 5), (20, 0), (0, 255, 0))
    ]
    space = Space(200, 200, central_object, orbital_objects, 'test_save_load')
    save_data(space)
    path = 'simulations/test_save_load/test_save_load.json'
    path_img = 'simulations/test_save_load/test_save_load.png'
    path_dir = 'simulations/test_save_load'
    with open(path, 'r') as file_handle:
        space = load_data(file_handle)
        assert space.size() == 200
        assert space.scale() == 200
        assert space.name() == 'test_save_load'
        assert space.central_object.mass() == 2000
        assert space.central_object.diameter() == 100
        assert space.orbital_objects[0].id() == 1
        assert space.orbital_objects[0].mass() == 200
        assert space.orbital_objects[0].position() == (2, 2)
        assert space.orbital_objects[0].velocity() == (20, 0)
        assert space.orbital_objects[1].id() == 2
        assert space.orbital_objects[1].mass() == 100
        assert space.orbital_objects[1].position() == (10, 5)
        assert space.orbital_objects[1].velocity() == (20, 0)
    os.remove(path)
    os.remove(path_img)
    os.rmdir(path_dir)
