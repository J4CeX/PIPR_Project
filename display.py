import os
from space import Space
import data


communique = '(Press Enter to continue)'


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
            print(f'Saving completed {communique}')
            input()
        elif after_simulation_option == '0':
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
        clean()
        print(space.info())
        input()
    elif option == '2':
        return
    else:
        wrong_option()


def show_results(space: Space):
    clean()
    print(space.info())
    print(f'Showing simulation results {communique}')
    input()
