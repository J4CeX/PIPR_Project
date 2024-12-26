from menu import load_data


def test_load_data():
    path = 'simulations/test1/test1.json'
    with open(path, 'r') as file_handle:
        space = load_data(file_handle)
        assert space.size() == 500
        assert space.space_name() == 'test1'
        assert space.central_object.mass() == 2000
        assert space.central_object.diameter() == 100
        assert space.orbital_objects[0].mass() == 200
        assert space.orbital_objects[0].position() == (2, 2)
        assert space.orbital_objects[0].velocity == 2
        assert space.orbital_objects[1].mass() == 100
        assert space.orbital_objects[1].position() == (10, 5)
        assert space.orbital_objects[1].velocity == 2
