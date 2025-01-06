from space import (
    Space,
    ValueIsNotStrError,
    ValueIsNotFloatError,
    ValueIsNotIntegerError,
    ValueIsNotPositiveError
)
from objects import OrbitalObject, CentralObject
import pytest


def test_Space_create():
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
    space = Space(500, 200.0, central_object, orbital_objects)
    assert space.size() == 500
    assert space.scale() == 200
    assert space.central_object.diameter() == 100
    assert space.central_object.mass() == 2000
    assert space.orbital_objects[0].mass() == 200
    assert space.orbital_objects[1].mass() == 100


def test_Space_create_wrong_types():
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
    with pytest.raises(ValueIsNotStrError):
        Space(500, 200.0, central_object, orbital_objects, 1)
    with pytest.raises(ValueIsNotIntegerError):
        Space(500.2, 200.0, central_object, orbital_objects)
    with pytest.raises(ValueIsNotFloatError):
        Space(500, 200, central_object, orbital_objects, 1)


def test_Space_create_not_positive_values():
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
    with pytest.raises(ValueIsNotPositiveError):
        Space(-1, 200.0, central_object, orbital_objects)
    with pytest.raises(ValueIsNotPositiveError):
        Space(0, 200.0, central_object, orbital_objects)
    with pytest.raises(ValueIsNotPositiveError):
        Space(500, -1.0, central_object, orbital_objects)
    with pytest.raises(ValueIsNotPositiveError):
        Space(500, 0.0, central_object, orbital_objects)


def test_Space_set_name():
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
    space = Space(500, 200, central_object, orbital_objects)
    assert space.name() == 'unknown'
    space.set_name('change')
    assert space.name() == 'change'


def test_Space_simulate():
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
    space = Space(200, 200, central_object, orbital_objects, 'test')
    space.simulate(1, 3600 * 24)


def test_Space_simulate_Earth_Sun():
    name = 'Sun_and_Earth_relative_scale'
    scale = 3e-9
    # based on image size, in real scale if one pixel is
    # 12756000 meters (earth diameter) then range between
    # Sun and Earth would be about 11728 pixels
    sun_mass = 1.989e30
    sun_diameter = 6.9634e8
    earth_mass = 5.972e24
    average_distance = 1.496e11
    velocityY = 29780.0
    central_object = CentralObject(sun_mass, sun_diameter)
    orbital_objects = [
        OrbitalObject(
            1,
            earth_mass,
            (average_distance, 0.0),
            (0.0, velocityY),
            (255, 0, 0))
    ]
    space = Space(1000, scale, central_object, orbital_objects, name)
    space.simulate(365, 3600 * 24)
    space.show_image()


'''WARNING! RUNNING THIS TEST MAY CRASH THE PROGRAM'''
# def test_Space_simulate_Earth_Sun_real():
#     # too big size
#     name = 'Sun_and_Earth_real'
#     scale = 1 / 1.2756e7
#     sun_mass = 1.989e30
#     sun_diameter = 6.9634e8
#     earth_mass = 5.972e24
#     average_distance = 1.496e11
#     velocityY = 29780.0
#     central_object = CentralObject(sun_mass, sun_diameter)
#     orbital_objects = [
#         OrbitalObject(
#             1,
#             earth_mass,
#             (average_distance, 0.0),
#             (0.0, velocityY),
#             (255, 0, 0))
#     ]
#     space = Space(24000, scale, central_object, orbital_objects, name)
#     space.simulate(365, 3600 * 24)
#     space.show_image()


def test_Space_simulate_Earth_Moon():
    name = 'Earth_and_Moon'
    scale = 1 / 1.7374e6
    earth_mass = 5.972e24
    earth_diameter = 1.2756e7
    moon_mass = 7.34e22
    average_distance = 3.84399e8
    velocityY = 1023.0
    central_object = CentralObject(earth_mass, earth_diameter)
    orbital_objects = [
        OrbitalObject(
            1,
            moon_mass,
            (average_distance, 0.0),
            (0.0, velocityY),
            (255, 0, 0))
    ]
    space = Space(600, scale, central_object, orbital_objects, name)
    space.simulate(365, 3600 * 24)
    space.show_image()


def test_Space_simulate_collision():
    name = 'Earth_and_Moon_collision'
    scale = 1 / 1.7374e6
    earth_mass = 5.972e24
    earth_diameter = 1.2756e7
    moon_mass = 7.34e22
    average_distance = 3.84399e8
    velocityY = 1023.0
    central_object = CentralObject(earth_mass, earth_diameter)
    orbital_objects = [
        OrbitalObject(
            1,
            moon_mass,
            (average_distance, 0.0),
            (0.0, velocityY),
            (255, 0, 0)),
        OrbitalObject(
            2,
            moon_mass,
            (average_distance, 0.0),
            (0.0, velocityY),
            (0, 255, 0)),
        OrbitalObject(
            3,
            moon_mass,
            (average_distance * 0.8, 0.0),
            (0.0, velocityY),
            (0, 0, 255)),
        OrbitalObject(
            4,
            moon_mass,
            (average_distance / 8, average_distance / 2),
            (0.0, velocityY*2),
            (120, 160, 100))
    ]
    space = Space(600, scale, central_object, orbital_objects, name)
    space.simulate(365, 3600 * 24)
    space.show_image()
