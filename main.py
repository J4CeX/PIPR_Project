from data import (
    new_data,
    load_data,
)
from display import (
    clean,
    wrong_option,
    show_results,
    simulation
)
import os
from PIL import Image


def main():
    while True:
        clean()
        print('Options:')
        print('1. New simulation')
        print('2. Load simulation')
        print('0. Exit')
        main_menu_option = input('>> ')
        if main_menu_option == '1':
            space = new_data()
            simulation(space)
        elif main_menu_option == '2':
            files = os.listdir('simulations')
            while True:
                clean()
                for index in range(0, len(files)):
                    print(f'{index+1}. {files[index]}')
                print('0. Back to main menu')
                load_file_option = int(input('>> '))
                if load_file_option > 0 and load_file_option <= len(files):
                    path = f'simulations/{files[load_file_option-1]}'
                    results_file = f'/{files[load_file_option-1]}.json'
                    with open(path + results_file, 'r') as file_handle:
                        space = load_data(file_handle)
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
                                simulation(space)
                                # możliwość edytowania prędkości oraz masy
                            elif load_option == '0':
                                break
                            else:
                                wrong_option()
                elif load_file_option == 0:
                    break
                else:
                    wrong_option()

        elif main_menu_option == '0':
            clean()
            print("Goodbye")
            return
        else:
            wrong_option()


if __name__ == "__main__":
    main()
