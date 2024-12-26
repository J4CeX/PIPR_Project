from space import Space
from objects import (
    OrbitalObject,
    CentralObject
)
import os
import json


def header():
    width = 50
    print('*' * width)
    print('SIMULATION OF MOTION IN A GRAVITATIONAL FIELD'.center(width))
    print('*' * width)


def clean():
    os.system('cls')
    header()


def wrong_option():
    print('There is no such option (Press Enter to continue)')
    input()


def new_data():
    clean()
    print('Field name:')
    field_name = str(input('>> '))
    print('Field size:')
    size = int(input('>> '))
    clean()
    print('Central object')
    print('Diameter:')
    CO_diameter = int(input('>> '))
    print('Mass:')
    CO_mass = int(input('>> '))
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
        OO_mass = int(input('>> '))
        print('Position:')
        OO_x = int(input('(x) >> '))
        OO_y = int(input('(y) >> '))
        OO_position = (OO_x, OO_y)
        print('Velocity:')
        OO_velocity = int(input('>> '))
        orbital_object = OrbitalObject(OO_mass, OO_position, OO_velocity)
        orbital_objects.append(orbital_object)
    clean()
    central_object = CentralObject(CO_mass, CO_diameter)
    return Space(size, central_object, orbital_objects, field_name)


def load_data(file_handle):
    data = json.load(file_handle)
    try:
        space_name = data['space_name']
        size = data['size']
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
        return Space(
            size,
            central_object,
            orbital_objects,
            space_name
        )
    except KeyError as e:
        raise KeyError() from e
    except Exception as e:
        raise Exception() from e
