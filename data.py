from space import Space
from objects import (
    OrbitalObject,
    CentralObject
)
from display import clean
import json
import os


def new_data():
    clean()
    print('Field name:')
    field_name = str(input('>> '))
    print('Field size:')
    size = float(input('>> '))
    print('Field scale (px:meters): ')
    scale = int(input('>> 1px:'))
    clean()
    print('Central object')
    print('Diameter:')
    CO_diameter = float(input('>> '))
    print('Mass:')
    CO_mass = float(input('>> '))
    orbital_objects = []
    clean()
    print('Orbital objects')
    print('Number of objects:')
    quantity = int(input('>> '))
    for index in range(0, quantity):
        clean()
        print('Orbital objects')
        print(f'Object: {index+1}.')
        print('Mass:')
        OO_mass = float(input('>> '))
        print('Position:')
        OO_x = int(input('(x) >> '))
        OO_y = int(input('(y) >> '))
        OO_position = (OO_x, OO_y)
        print('Velocity:')
        OO_velocity = float(input('>> '))
        orbital_object = OrbitalObject(OO_mass, OO_position, OO_velocity)
        orbital_objects.append(orbital_object)
    clean()
    central_object = CentralObject(CO_mass, CO_diameter)
    return Space(size, scale, central_object, orbital_objects, field_name)


def load_data(file_handle):
    data = json.load(file_handle)
    try:
        space_name = data['space_name']
        size = data['size']
        scale = data['scale']
        loaded_central_object = data['central_object']
        loaded_orbital_objects = data['orbital_objects']
        central_object = CentralObject(
            loaded_central_object['mass'],
            loaded_central_object['diameter']
        )
        orbital_objects = []
        for object in loaded_orbital_objects:
            orbital_objects.append(OrbitalObject(
                object['mass'],
                tuple(object['position']),
                object['velocity']
            ))
        return Space(size, scale, central_object, orbital_objects, space_name)
    except KeyError as e:
        raise KeyError() from e
    except Exception as e:
        raise Exception() from e


def save_data(space: Space):
    name = space.space_name()
    directory = f'{name}'
    parent_dir = 'simulations'
    path_directory = os.path.join(parent_dir, directory)
    os.mkdir(path_directory)  # rozwiązać problem z istniejącym plikiem
    path_image = f'simulations/{name}/{name}.png'
    space._space_image.save(path_image)
    path_results = f'simulations/{name}/{name}.json'
    orbital_objects = []
    for object in space.orbital_objects:
        object_data = {
            'mass': object.mass(),
            'position': object.position(),
            'velocity': object.velocity
        }
        orbital_objects.append(object_data)
    with open(path_results, 'w') as file_handle:
        size = space.size()
        scale = space.scale()
        central_object = space.central_object
        results = {
            'space_name': name,
            'size': size,
            'scale': scale,
            'central_object': {
                'mass': central_object.mass(),
                'diameter': central_object.diameter()
            },
            'orbital_objects': orbital_objects
        }
        json.dump(results, file_handle, indent=4)
