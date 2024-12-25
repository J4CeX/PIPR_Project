from menu import (
    main_menu_print,
    new_data,
    load_data,
    clean,
    wrong_option
)
import os


def main():
    while True:
        os.system('cls')
        main_menu_print()
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
                print('0. Return to main menu')
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
            # wczytywanie wyników poprzedniej symulacji
            space = load_data()
        elif main_menu_option == '0':
            print("Goodbye")
            return
        else:
            wrong_option()


if __name__ == "__main__":
    main()
