from objects import (
    Object,
    OrbitalObject,
    CentralObject,
    ValueIsNotFloatError,
    ValueIsNotPositiveError,
    ValueIsNotIntegerError,
    RGBValueError
)
import pytest


def test_Object_create():
    object = Object(200.0, (20.0, 20.0))
    assert object.mass() == 200.0
    assert object.position() == (20.0, 20.0)


def test_Object_create_wrong_types():
    with pytest.raises(ValueIsNotFloatError):
        Object('200', (20, 20))
    with pytest.raises(ValueIsNotFloatError):
        Object(200, ('20', 20))
    with pytest.raises(ValueIsNotFloatError):
        Object(200, (20, '20'))


def test_Object_create_not_positive_mass():
    with pytest.raises(ValueIsNotPositiveError):
        Object(-1.0, (20.0, 20.0))
    with pytest.raises(ValueIsNotPositiveError):
        Object(0.0, (20.0, 20.0))


def test_Object_set_positon():
    object = Object(200.0, (20.0, 20.0))
    assert object.position() == (20.0, 20.0)
    object.set_position((10.0, 10.0))
    assert object.position() == (10.0, 10.0)


def test_Object_set_positon_wrong_type():
    object = Object(200.0, (20.0, 20.0))
    with pytest.raises(ValueIsNotFloatError):
        object.set_position((20, 20.42))
    with pytest.raises(ValueIsNotFloatError):
        object.set_position((20.24, 20))


def test_Central_Object_create():
    object = CentralObject(2000.0, 200.0)
    assert object.mass() == 2000.0
    assert object.diameter() == 200.0
    assert object.position() == (0.0, 0.0)


def test_Central_Object_create_wrong_diameter_type():
    with pytest.raises(ValueIsNotFloatError):
        CentralObject(200.0, '20.0')


def test_Central_Object_create_not_positive_diameter():
    with pytest.raises(ValueIsNotPositiveError):
        CentralObject(200.0, 0.0)
    with pytest.raises(ValueIsNotPositiveError):
        CentralObject(200.0, -1.0)


def test_Central_Object_position():
    object = CentralObject(2000.0, 200.0)
    assert object.position() == (0.0, 0.0)
    object.set_position((250.0, 250.0))
    assert object.position() == (250.0, 250.0)


def test_Orbital_Object_create():
    object = OrbitalObject(
        1, 200.0, (2.0, 3.0),
        (20.0, 0.0), (255, 0, 0)
    )
    assert object.id() == 1.0
    assert object.mass() == 200.0
    assert object.velocity() == (20.0, 0.0)
    assert object.position() == (2.0, 3.0)
    assert object.pixel() == (None, None)
    assert object.color == (255, 0, 0)


def test_Orbital_Object_create_wrong_types():
    with pytest.raises(ValueIsNotIntegerError):
        OrbitalObject(
            1.2, 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0, 0)
        )
    with pytest.raises(ValueIsNotIntegerError):
        OrbitalObject(
            '1', 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0, 0)
        )
    with pytest.raises(ValueIsNotFloatError):
        OrbitalObject(
            1, 200.0, (2.0, 3.0),
            ('20.0', 0.0), (255, 0, 0)
        )
    with pytest.raises(ValueIsNotFloatError):
        OrbitalObject(
            1, 200.0, (2.0, 3.0),
            (20.0, '0.0'), (255, 0, 0)
        )
    with pytest.raises(ValueIsNotIntegerError):
        OrbitalObject(
            1, 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0.5, 0)
        )
    with pytest.raises(ValueIsNotIntegerError):
        OrbitalObject(
            1, 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0.5, '0')
        )


def test_Orbital_Object_create_not_positive():
    with pytest.raises(ValueIsNotPositiveError):
        OrbitalObject(
            0, 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0, 0)
        )
    with pytest.raises(ValueIsNotPositiveError):
        OrbitalObject(
            -1, 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0, 0)
        )
    with pytest.raises(ValueIsNotPositiveError):
        OrbitalObject(
            1, -1.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0, 0)
        )


def test_Orbital_Object_create_RGB_wrong_range():
    with pytest.raises(RGBValueError):
        OrbitalObject(
            1, 200.0, (2.0, 3.0),
            (20.0, 0.0), (256, 0, 0)
        )
    with pytest.raises(RGBValueError):
        OrbitalObject(
            1, 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, -1, 0)
        )
    with pytest.raises(RGBValueError):
        OrbitalObject(
            1, 200.0, (2.0, 3.0),
            (20.0, 0.0), (255, 0, -255)
        )


def test_Orbital_Object_set_pixel():
    object = OrbitalObject(
        1, 200.0, (2.0, 3.0),
        (20.0, 0.0), (255, 0, 0)
    )
    assert object.pixel() == (None, None)
    object.set_pixel((3, 3))
    assert object.pixel() == (3, 3)


def test_Orbital_Object_set_pixel_wrong_type():
    object = OrbitalObject(
        1, 200.0, (2.0, 3.0),
        (20.0, 0.0), (255, 0, 0)
    )
    with pytest.raises(ValueIsNotIntegerError):
        object.set_pixel((20.2, 20))
    with pytest.raises(ValueIsNotIntegerError):
        object.set_pixel((20, 20.3))
