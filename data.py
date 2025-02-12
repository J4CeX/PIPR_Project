from space import (
    Space,
    OrbitalObject,
    CentralObject
)
from random import randint
from display import (
    clean,
    wrong_option,
    WIDTH,
    communique
)
from inputs import (
    int_input,
    float_input,
    positive_float_input,
    RGB_input
)
import json
import os


def field_data():
    """
    Collects data about space field.
    """
    print('Field name:')
    field_name = str(input('>> '))
    print('Field size:')
    size = int_input()
    print('Field scale (px:meters): ')
    meters = positive_float_input('1px ')
    scale = 1 / meters
    return field_name, size, scale


def central_object_data():
    """
    Collects data about central object.
    """
    print('Central object')
    print('Diameter (meters):')
    CO_diameter = positive_float_input()
    print('Mass (kilograms):')
    CO_mass = positive_float_input()
    return CentralObject(CO_mass, CO_diameter)


def orbital_objects_data(CO_mass):
    """
    Collects data about orbital objects.
    """
    orbital_objects = []
    print('Orbital objects')
    print('Number of objects:')
    quantity = int_input()
    message = 'Central point of the central object is placed on x=0, y=0'
    for id in range(1, quantity+1):
        print('*' * WIDTH)
        print('Objects are placed on a Cartesian plane'.center(WIDTH))
        print(message.center(WIDTH))
        print('*' * WIDTH)
        print('Orbital objects')
        print('Object:')
        print(f'Id: {id}')
        print('Mass (kilograms):')
        while True:
            OO_mass = positive_float_input()
            if OO_mass >= CO_mass:
                print("Orbital object's mass cannot be bigger than Central's")
            else:
                break
        msg = '(real distance in meters, for instance average radius and zero)'
        print(f'Position {msg}:')
        OO_x = float_input('(x) ')
        OO_y = float_input('(y) ')
        OO_position = (OO_x, OO_y)
        print('Velocity (meters per second):')
        OO_velocity_x = float_input('(x) ')
        OO_velocity_y = float_input('(y) ')
        OO_velocity = (OO_velocity_x, OO_velocity_y)
        color = None
        while True:
            clean()
            print(f'Id: {id}')
            print('Color:')
            print('1. Red')
            print('2. Blue')
            print('3. Yellow')
            print('4. Green')
            print('5. Pink')
            print('6. Orange')
            print('7. RGB')
            print('8. Random')
            color_option = input('>> ')
            if color_option == '1':
                color = (255, 0, 0)
                break
            elif color_option == '2':
                color = (0, 0, 255)
                break
            elif color_option == '3':
                color = (255, 200, 0)
                break
            elif color_option == '4':
                color = (0, 255, 0)
                break
            elif color_option == '5':
                color = (255, 100, 200)
                break
            elif color_option == '6':
                color = (255, 165, 0)
                break
            elif color_option == '7':
                color = RGB_input()
                break
            elif color_option == '8':
                R = int(randint(125, 255))
                G = int(randint(125, 255))
                B = int(randint(125, 255))
                color = (R, G, B)
                break
            else:
                wrong_option()
        clean()
        orbital_object = OrbitalObject(id, OO_mass, OO_position,
                                       OO_velocity, color)
        orbital_objects.append(orbital_object)
    return orbital_objects


def new_data():
    """
    Collects data and generate new Space object.
    """
    clean()
    field_name, size, scale = field_data()
    clean()
    central_object = central_object_data()
    clean()
    orbital_objects = orbital_objects_data(central_object.mass())
    clean()
    return Space(size, scale, central_object, orbital_objects, field_name)


def load_data(file_handle):
    """
    Loads previously saved data and enters it into the program.
    """
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
                object['id'],
                object['mass'],
                tuple(object['position']),
                tuple(object['velocity']),
                tuple(object['color'])
            ))
        collisions = data['collisions']
        return Space(size, scale, central_object,
                     orbital_objects, name, collisions)
    except KeyError as e:
        raise KeyError() from e
    except Exception as e:
        raise Exception() from e


def save_data(space: Space):
    """
    Saves data about the simulation performed into json file.
    """
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
        """Handling with existing files"""
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
                return
            else:
                wrong_option()

    space._image.save(path_image)
    orbital_objects = []
    for object in space.orbital_objects:
        object_data = {
            'id': object.id(),
            'mass': object.mass(),
            'position': object.position(),
            'velocity': object.velocity(),
            'color': object.color
        }
        orbital_objects.append(object_data)
    with open(path_results, 'w') as file_handle:
        size = space.size()
        scale = space.scale()
        central_object = space.central_object
        collisions = space.collisions
        results = {
            'name': name,
            'size': size,
            'scale': scale,
            'central_object': {
                'mass': central_object.mass(),
                'diameter': central_object.diameter()
            },
            'orbital_objects': orbital_objects,
            'collisions': collisions
        }
        json.dump(results, file_handle, indent=6)
    print(f'Saving completed {communique}')
    input()


def edit_data(space: Space):
    """
    Allows editing of loaded simulation data.
    """
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
            CO_mass = space.central_object.mass()
            space.orbital_objects = orbital_objects_data(CO_mass)
            break
        elif option == '0':
            clean()
            print(f'Editing abandoned {communique}')
            input()
            return
        else:
            wrong_option()
