from space import Space
from objects import OrbitalObject, CentralObject
from PIL import Image
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
    clean()
    print('Enter steps number: ')
    steps = int(input('>> '))
    space.simulate(steps)
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
    files = os.listdir('simulations')
    while True:
        clean()
        for index in range(0, len(files)):
            print(f'{index+1}. {files[index]}')
        print('0. Back to main menu')
        load_file_option = int(input('>> '))  # problem
        if load_file_option > 0 and load_file_option <= len(files):
            path = f'simulations/{files[load_file_option-1]}'
            results_file = f'/{files[load_file_option-1]}.json'
            with open(path + results_file, 'r') as file_handle:
                space = data.load_data(file_handle)
                input()
            while True:
                clean()
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
                    edit(space)
                    simulation(space)
                elif load_option == '0':
                    break
                else:
                    wrong_option()
        elif load_file_option == 0:
            break
        else:
            wrong_option()


def edit(space: Space):
    clean()
    print('Would you like to edit any values?')
    print('1. Yes')
    print('2. No')
    option = input('>> ')
    if option == '1':
        data.edit_data(space)
    elif option == '2':
        return
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
                    moon_mass,
                    (average_distance, 0),
                    (0, velocityY))
            ]
            space = Space(600, scale, central_object, orbital_objects, name)
            simulation(space)
            return
        elif option == '0':
            return
        else:
            wrong_option()
