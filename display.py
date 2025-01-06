from space import Space
from objects import (
    OrbitalObject,
    CentralObject
)
from PIL import Image
from inputs import int_input
import data
import os


communique = '(Press Enter to continue)'

WIDTH = 60


def header():
    print('*' * WIDTH)
    print('SIMULATION OF MOTION IN A GRAVITATIONAL FIELD'.center(WIDTH))
    print('*' * WIDTH)


def clean():
    os.system('cls')
    header()


def wrong_option():
    print('There is no such option (Press Enter to continue)')
    input()


def simulation(space):
    """
    Prints simulation interface.
    Takes the simulation time period and runs the simulation.
    """
    time = None
    while True:
        clean()
        print('Enter time unit for one step: ')
        print('1. Days')
        print('2. Hours')
        print('3. Minutes')
        print('4. Seconds')
        print('5. Custom')
        option = input('>> ')
        if option == '1':
            time = 3600 * 24
            break
        elif option == '2':
            time = 3600
            break
        elif option == '3':
            time = 60
            break
        elif option == '4':
            time = 1
            break
        elif option == '5':
            time = int_input('seconds ')
            break
        else:
            wrong_option()
    print('Enter steps number: ')
    steps = int_input()
    space.simulate(steps, time)
    while True:
        clean()
        print('Options:')
        print('1. Show simulation results')
        print('2. Show simulation graphics')
        print('3. Save results to file')
        print('0. Cancel')
        after_simulation_option = input('>> ')
        clean()
        if after_simulation_option == '1':
            show_results(space)
        elif after_simulation_option == '2':
            space.show_image()
            print(f'Showing simulation graphic {communique}')
            input()
        elif after_simulation_option == '3':
            data.save_data(space)
        elif after_simulation_option == '0':
            break
        else:
            wrong_option()


def load_simulation():
    """
    Prints load simulation interface.
    """
    try:
        files = os.listdir('simulations')
    except FileNotFoundError:
        clean()
        print(f'No simulations found {communique}')
        input()
        return
    while True:
        clean()
        for index in range(0, len(files)):
            print(f'{index+1}. {files[index]}')
        print('0. Cancel')
        load_file_option = int_input()  # problem
        if load_file_option > 0 and load_file_option <= len(files):
            path = f'simulations/{files[load_file_option-1]}'
            results_file = f'/{files[load_file_option-1]}.json'
            with open(path + results_file, 'r') as file_handle:
                space = data.load_data(file_handle)
            while True:
                clean()
                print('Options:')
                print('1. Show simulation results')
                print('2. Show simulation graphics')
                print('3. Start new simulation from the last step')
                print('0. Cancel')
                load_option = input('>> ')
                if load_option == '1':
                    show_results(space)
                elif load_option == '2':
                    img_file = f'/{files[load_file_option-1]}.png'
                    image = Image.open(path + img_file)
                    image.show()
                elif load_option == '3':
                    if edit(space):
                        simulation(space)
                    break
                elif load_option == '0':
                    break
                else:
                    wrong_option()
        elif load_file_option == 0:
            break
        else:
            wrong_option()


def edit(space: Space):
    while True:
        clean()
        print('Would you like to edit any values?')
        print('1. Yes')
        print('2. No')
        print('0. Cancel')
        option = input('>> ')
        if option == '1':
            data.edit_data(space)
            return True
        elif option == '2':
            return True
        elif option == '0':
            return False
        else:
            wrong_option()


def show_results(space: Space):
    clean()
    print(space.info())
    print(f'Showing simulation results {communique}')
    input()


def sample_simulations():
    while True:
        clean()
        print('Sample simulations:')
        print('1. Earth and Moon ')
        print('0. Cancel')
        option = input('>> ')
        if option == '1':
            name = 'Earth_and_Moon_simulation'
            scale = 1 / 1.7374e6
            earth_mass = 5.972e24
            earth_diameter = 1.2756e7
            moon_mass = 7.34e22
            average_distance = 3.84399e8
            velocityY = 1023
            central_object = CentralObject(earth_mass, earth_diameter)
            orbital_objects = [
                OrbitalObject(
                    1,
                    moon_mass,
                    (average_distance, 0),
                    (0, velocityY),
                    (255, 255, 255)
                )
            ]
            space = Space(600, scale, central_object, orbital_objects, name)
            simulation(space)
            break
        elif option == '0':
            break
        else:
            wrong_option()
