from space import Space
from objects import (
    OrbitalObject,
    CentralObject
)
from display import (
    clean,
    wrong_option
)
import json
import os


def new_data():
    clean()
    print('Field name:')
    field_name = str(input('>> '))
    print('Field size:')
    size = int(input('>> '))
    print('Field scale (px:meters): ')
    scale = 1 / float(input('>> 1px:'))
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
        OO_x = float(input('(x) >> '))
        OO_y = float(input('(y) >> '))
        OO_position = (OO_x, OO_y)
        print('Velocity:')
        OO_velocity_x = float(input('(x) >> '))
        OO_velocity_y = float(input('(y) >> '))
        OO_velocity = (OO_velocity_x, OO_velocity_y)
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
                tuple(object['velocity'])
            ))
        return Space(size, scale, central_object, orbital_objects, space_name)
    except KeyError as e:
        raise KeyError() from e
    except Exception as e:
        raise Exception() from e


def save_data(space: Space):
    communique = '(Press Enter to continue)'
    name = space.space_name()
    directory = f'{name}'
    parent_dir = 'simulations'
    path_directory = os.path.join(parent_dir, directory)
    path_image = f'simulations/{name}/{name}.png'
    path_results = f'simulations/{name}/{name}.json'
    if not os.path.isdir(parent_dir):
        os.mkdir(parent_dir)
    if not os.path.isdir(path_directory):
        os.mkdir(path_directory)
    else:
        while True:
            clean()
            print('Simulation of space with such name already exist.')
            print('1. Rename space name')
            print('2. Replace file (Delete previous results)')
            print('0. Cancel')
            option = input('>> ')
            if option == '1':
                while True:
                    clean()
                    print('Renaming Space name (leave empty to cancel):')
                    new_name = input('>> ')
                    if new_name == '':
                        clean()
                        print(f'Renaming canceled {communique}')
                        input()
                        break
                    elif new_name != space.space_name():
                        space.set_space_name(new_name)
                        print(f'Successful name change {communique}')
                        input()
                        return
                    else:
                        clean()
                        print(f'New name has to be different! {communique}')
                        input()
            elif option == '2':
                if os.path.isfile(path_image):
                    os.remove(path_image)
                if os.path.isfile(path_results):
                    os.remove(path_results)
                os.rmdir(path_directory)
                os.mkdir(path_directory)
                break
            elif option == '0':
                print(f'Saving abonded {communique}')
                input()
            else:
                wrong_option()

    space._space_image.save(path_image)
    orbital_objects = []
    for object in space.orbital_objects:
        object_data = {
            'mass': object.mass(),
            'position': object.position(),
            'velocity': object.velocity()
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
        json.dump(results, file_handle, indent=5)
    print(f'Saving completed {communique}')
    input()
