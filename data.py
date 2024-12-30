from space import Space
from objects import (
    OrbitalObject,
    CentralObject
)
from display import (
    clean,
    wrong_option,
    WIDTH,
    communique
)
import json
import os


def field_data():
    print('Field name:')
    field_name = str(input('>> '))
    print('Field size:')
    size = int(input('>> '))
    print('Field scale (px:meters): ')
    scale = 1 / float(input('>> 1px:'))
    return field_name, size, scale


def central_object_data():
    print('Central object')
    print('Diameter (meters):')
    CO_diameter = float(input('>> '))
    print('Mass (kilograms):')
    CO_mass = float(input('>> '))
    return CentralObject(CO_mass, CO_diameter)


def orbital_objects_data():
    orbital_objects = []
    print('Orbital objects')
    print('Number of objects:')
    quantity = int(input('>> '))
    message = 'Central point of the central object is placed on x=0, y=0'
    print('*' * WIDTH)
    print('Objects are placed on a Cartesian plane'.center(WIDTH))
    print(message.center(WIDTH))
    print('*' * WIDTH)
    print('Orbital objects')
    for index in range(0, quantity):
        print()
        print(f'Object: {index+1}.')
        print('Mass (kilograms):')
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
    return orbital_objects


def new_data():
    clean()
    field_name, size, scale = field_data()
    clean()
    central_object = central_object_data()
    clean()
    orbital_objects = orbital_objects_data()
    clean()
    return Space(size, scale, central_object, orbital_objects, field_name)


def load_data(file_handle):
    data = json.load(file_handle)
    try:
        name = data['name']
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
        return Space(size, scale, central_object, orbital_objects, name)
    except KeyError as e:
        raise KeyError() from e
    except Exception as e:
        raise Exception() from e


def save_data(space: Space):
    name = space.name()
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
            clean()
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
                    elif new_name != space.name():
                        space.set_name(new_name)
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
                print(f'Saving abandoned {communique}')
                input()
            else:
                wrong_option()

    space._image.save(path_image)
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
            'name': name,
            'size': size,
            'scale': scale,
            'central_object': {
                'mass': central_object.mass(),
                'diameter': central_object.diameter()
            },
            'orbital_objects': orbital_objects
        }
        json.dump(results, file_handle, indent=5)


def edit_data(space: Space):
    def header():
        print('Data editing'.center(WIDTH))
        print('-' * WIDTH)
        print(space.info())
        print('-' * WIDTH)
    clean()
    header()
    print('1. Edit field')
    print('2. Edit central object')
    print('3. Edit Orbital objects')
    print('0. Cancel')
    option = input('>> ')
    clean()
    header()
    while True:
        if option == '1':
            field_name, size, scale = field_data()
            space.set_name(field_name)
            space.set_size(size)
            space.set_scale(scale)
            break
        elif option == '2':
            space.central_object = central_object_data()
            break
        elif option == '3':
            space.orbital_objects = orbital_objects_data()
            break
        elif option == '0':
            clean()
            print(f'Editing abandoned {communique}')
            input()
            return
        else:
            wrong_option()
