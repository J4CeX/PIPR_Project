from simulation import Simulation
from space import Space
from objects import OrbitalObject, CentralObject


def test_Simulation_create():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), 2),
        OrbitalObject(100, (10, 5), 2)
    ]
    space = Space(500, central_object, orbital_objects, 'test')
    simulation = Simulation(space)
    assert simulation.space.central_object == central_object
    assert simulation.space.orbital_objects == orbital_objects
    assert simulation.space.space_name() == 'test'
    assert simulation.space.size() == 500


def test_Simulation_simulate():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), 2),
        OrbitalObject(100, (10, 5), 2)
    ]
    space = Space(500, central_object, orbital_objects, 'test')
    simulation = Simulation(space)
    simulation.simulate()


def test_Simulation_save():
    central_object = CentralObject(2000, 100)
    orbital_objects = [
        OrbitalObject(200, (2, 2), 2),
        OrbitalObject(100, (10, 5), 2)
    ]
    space = Space(500, central_object, orbital_objects, 'test')
    simulation = Simulation(space)
    simulation.save()
