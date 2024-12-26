from objects import OrbitalObject, CentralObject


def test_Central_Object_create():
    object = CentralObject(2000, 200)
    assert object.mass() == 2000
    assert object.diameter() == 200


def test_Central_Object_position():
    object = CentralObject(2000, 200)
    assert object.position() == (0, 0)
    object.set_position((250, 250))
    assert object.position() == (250, 250)


def test_Orbital_Object_create():
    object = OrbitalObject(200, (2, 2), 20)
    assert object.mass() == 200
    assert object.x == 2
    assert object.y == 2
    assert object.velocity == 20
    assert object.position() == (2, 2)
