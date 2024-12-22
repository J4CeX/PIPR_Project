from objects import OrbitalObject, CentralObject


def test_Central_Object_create():
    object = CentralObject(2000, 200)
    assert object.mass() == 2000
    assert object.diameter() == 200


def test_Orbital_Object_create():
    object = OrbitalObject(200, 'north-east', 20)
    assert object.mass() == 200
    assert object.positon == 'north-east'
    assert object.speedVector == 20
