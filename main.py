from menu import (
    new_data,
    load_data,
    clean,
    wrong_option
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
            print('Enter steps number: ')
            steps = int(input('>> '))
            space.simulate(steps)
            while True:
                clean()
                print('Options:')
                print('1. Save results to file')
                print('2. Show simulation graphics')
                print('0. Back to main menu')
                after_simulation_option = input('>> ')
                clean()
                communique = '(Press Enter to continue)'
                if after_simulation_option == '1':
                    space.save()
                    print(f'Saving completed {communique}')
                    input()
                elif after_simulation_option == '2':
                    space.show()
                    print(f'Showing simulation graphics {communique}')
                    input()
                elif after_simulation_option == '0':
                    break
                else:
                    wrong_option()
        elif main_menu_option == '2':
            files = os.listdir('simulations')
            while True:
                clean()
                for index in range(0, len(files)):
                    print(f'{index+1}. {files[index]}')
                print('0. Back to main menu')
                load_file_option = int(input('>> '))  # tylko jeden znak
                if load_file_option > 0 and load_file_option <= len(files):
                    path = f'simulations/{files[load_file_option-1]}'
                    while True:
                        clean()
                        print('1. Show graph')
                        print('2. Show results')
                        print('3. Start new simulation from the last step')
                        print('0. Cancel')
                        load_option = input('>> ')
                        if load_option == '1':
                            path += f'/{files[load_file_option-1]}.png'
                            image = Image.open(path)
                            image.show()
                        elif load_option == '2':
                            path += f'/{files[load_file_option-1]}.json'
                            with open(path, 'r') as file_handle:
                                # space =
                                load_data(file_handle)
                        elif load_option == '3':
                            pass
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
