from space import Space
from objects import OrbitalObject, CentralObject


def test_Space_create():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), (20, 0)),
        OrbitalObject(100, (10, 5), (20, 0))
    ]
    space = Space(500, 200, central_object, orbital_objects)
    assert space.size() == 500
    assert space.scale() == 200
    assert space.central_object.diameter() == 100
    assert space.central_object.mass() == 2000
    assert space.orbital_objects[0].mass() == 200
    assert space.orbital_objects[1].mass() == 100


def test_Space_set_space_name():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), (20, 0)),
        OrbitalObject(100, (10, 5), (20, 0))
    ]
    space = Space(500, 200, central_object, orbital_objects)
    assert space.space_name() == 'unknown'
    space.set_space_name('change')
    assert space.space_name() == 'change'


def test_Space_simulate():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), (20, 0)),
        OrbitalObject(100, (10, 5), (20, 0))
    ]
    space = Space(200, 200, central_object, orbital_objects, 'test')
    space.simulate(1)


def test_Space_simulate_Earth_Sun():
    scale = 3e-9  # based on image size, in real scale if one pixel is 12756000 meters (earth diameter) then range between Sun and Earth would be about 11728 pixels
    sun_mass = 1.989e30
    sun_diameter = 6.9634e8
    earth_mass = 5.972e24
    average_distance = 1.496e11
    velocityY = 29780
    central_object = CentralObject(sun_mass, sun_diameter)
    orbital_objects = [
        OrbitalObject(
            earth_mass,
            (average_distance, 0),
            (0, velocityY))
    ]
    space = Space(1000, scale, central_object, orbital_objects, 'test_test')
    space.simulate(365)
    space.show_image()


def test_Space_simulate_Earth_Sun_real():
    # za duży wymiar
    scale = 1 / 1.2756e7
    sun_mass = 1.989e30
    sun_diameter = 6.9634e8
    earth_mass = 5.972e24
    average_distance = 1.496e11
    velocityY = 29780
    central_object = CentralObject(sun_mass, sun_diameter)
    orbital_objects = [
        OrbitalObject(
            earth_mass,
            (average_distance, 0),
            (0, velocityY))
    ]
    space = Space(24000, scale, central_object, orbital_objects, 'test_test')
    space.simulate(365)
    space.show_image()


def test_Space_simulate_Earth_Moon():
    scale = 1 / 1.7374e6
    earth_mass = 5.972e24
    earth_diameter = 1.2756e7
    moon_mass = 7.34e22
    average_distance = 3.84399e8
    velocityY = 1023
    central_object = CentralObject(earth_mass, earth_diameter)
    orbital_objects = [
        OrbitalObject(
            moon_mass,
            (average_distance, 0),
            (0, velocityY))
    ]
    space = Space(600, scale, central_object, orbital_objects, 'test_test')
    space.simulate(365)
    space.show_image()
