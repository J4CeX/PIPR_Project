from space import Space
from objects import (
    OrbitalObject,
    CentralObject
)
import os


def menu_print(width):
    print('*' * width)
    print('SIMULATION OF MOTION IN A GRAVITATIONAL FIELD'.center(width))
    print('*' * width)
    print('Options:')
    print('1. New simulation')
    print('2. Load simulation')
    print('0. Exit')


def new_data():
    print('Field name:')
    field_name = str(input('>> '))
    print('Field size:')
    size = int(input('>> '))
    print('Central object')
    print('Diameter:')
    CO_diameter = int(input('>> '))
    print('Mass:')
    CO_mass = int(input('>> '))
    orbital_objects = []
    print('Orbital objects')
    print('Number of objects:')
    quantity = int(input('>> '))
    for index in range(0, quantity):
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
    os.system('cls')
    central_object = CentralObject(CO_mass, CO_diameter)
    return Space(size, central_object, orbital_objects, field_name)


def load_data():
    pass


def main():
    width = 40
    while True:
        os.system('cls')
        menu_print(width)
        option = input('>> ')
        if option == '1':
            space = new_data()
            print('Enter steps number: ')
            steps = int(input('>> '))
            space.simulate(steps)
        elif option == '2':
            # wczytywanie wyników poprzedniej symulacji
            space = load_data()
        elif option == '0':
            print("Goodbye")
            return
        else:
            print('There is no such option (Press Enter to continue)')
            input()


if __name__ == "__main__":
    main()
