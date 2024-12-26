import os
from space import Space
import data


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


def saving_completed_communique():
    communique = '(Press Enter to continue)'
    print(f'Saving completed {communique}')
    input()


def showing_graphic_communique():
    communique = '(Press Enter to continue)'
    print(f'Showing simulation graphic {communique}')
    input()


def simulation(space):
    print('Enter steps number: ')
    steps = int(input('>> '))
    space.simulate(steps)
    while True:
        clean()
        print('Options:')
        print('1. Show simulation results')
        print('2. Show simulation graphics')
        print('3. Save results to file')
        print('0. Back to main menu')
        after_simulation_option = input('>> ')
        clean()

        if after_simulation_option == '1':
            pass
        elif after_simulation_option == '2':
            space.show_image()
            showing_graphic_communique()
        elif after_simulation_option == '3':
            data.save_data(space)
            saving_completed_communique()
        elif after_simulation_option == '0':
            break
        else:
            wrong_option()


def show_results(space: Space):
    pass
