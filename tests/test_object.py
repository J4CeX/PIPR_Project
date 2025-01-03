from objects import (
    OrbitalObject,
    CentralObject
)
import pytest


def test_Central_Object_create():
    object = CentralObject(2000, 200)
    assert object.mass() == 2000
    assert object.diameter() == 200
    assert object.position() == (0, 0)


def test_Central_Object_position():
    object = CentralObject(2000, 200)
    assert object.position() == (0, 0)
    object.set_position((250, 250))
    assert object.position() == (250, 250)


def test_Orbital_Object_create():
    object = OrbitalObject(1, 200, (2, 3), (20, 0), (255, 0, 0))
    assert object.id() == 1
    assert object.mass() == 200
    assert object.velocity() == (20, 0)
    assert object.position() == (2, 3)
    assert object.pixel() == (None, None)
    assert object.color == (255, 0, 0)


def test_Orbital_Object_set_pixel():
    object = OrbitalObject(1, 200, (2, 3), (20, 0), (255, 0, 0))
    assert object.pixel() == (None, None)
    object.set_pixel((3, 3))
    assert object.pixel() == (3, 3)


def test_Orbital_Object_create_negative_id():
    with pytest.raises(ValueError):
        OrbitalObject(-1, 200, (2, 3), (20, 0), (255, 0, 0))
