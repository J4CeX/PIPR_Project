from data import (
    load_data,
    save_data,
    int_input,
    float_input,
    positive_float_input,
    RGB_input
)
from objects import (
    CentralObject,
    OrbitalObject
)
from space import Space
import os


def test_load_and_save_data(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: '')
    central_object = CentralObject(2000.0, 100.0)
    orbital_objects = [
        OrbitalObject(
            1, 200.0, (2.0, 2.0),
            (20.0, 0.0), (255, 0, 0)
        ),
        OrbitalObject(
            2, 100.0, (10.0, 5.0),
            (20.0, 0.0), (255, 0, 0)
        )
    ]
    space = Space(200, 200, central_object, orbital_objects, 'test_save_load')
    save_data(space)
    path = 'simulations/test_save_load/test_save_load.json'
    path_img = 'simulations/test_save_load/test_save_load.png'
    path_dir = 'simulations/test_save_load'
    with open(path, 'r') as file_handle:
        loaded_space = load_data(file_handle)
        assert loaded_space.size() == 200
        assert loaded_space.scale() == 200
        assert loaded_space.name() == 'test_save_load'
        assert loaded_space.central_object.mass() == 2000
        assert loaded_space.central_object.diameter() == 100
        assert loaded_space.orbital_objects[0].id() == 1
        assert loaded_space.orbital_objects[0].mass() == 200
        assert loaded_space.orbital_objects[0].position() == (2, 2)
        assert loaded_space.orbital_objects[0].velocity() == (20, 0)
        assert loaded_space.orbital_objects[1].id() == 2
        assert loaded_space.orbital_objects[1].mass() == 100
        assert loaded_space.orbital_objects[1].position() == (10, 5)
        assert loaded_space.orbital_objects[1].velocity() == (20, 0)
    os.remove(path)
    os.remove(path_img)
    os.rmdir(path_dir)


def test_int_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: '2')
    value = int_input()
    assert value == 2


def test_float_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: '2.3')
    value = float_input()
    assert value == 2.3
    monkeypatch.setattr('builtins.input', lambda x: '-2.3')
    value = float_input()
    assert value == -2.3


def test_positive_float(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: '2.3')
    value = positive_float_input()
    assert value == 2.3


def test_RGB_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: '125')
    value = RGB_input()
    assert value == (125, 125, 125)
