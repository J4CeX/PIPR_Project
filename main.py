from data import new_data
from display import (
    clean,
    wrong_option,
    simulation,
    load_simulation,
    sample_simulations
)


def main():
    while True:
        clean()
        print('Options:')
        print('1. New simulation')
        print('2. Load simulation')
        print('3. Sample simulations')
        print('0. Exit')
        main_menu_option = input('>> ')
        if main_menu_option == '1':
            space = new_data()
            simulation(space)
        elif main_menu_option == '2':
            load_simulation()
        elif main_menu_option == '3':
            sample_simulations()
        elif main_menu_option == '0':
            clean()
            print("Goodbye")
            return
        else:
            wrong_option()


if __name__ == "__main__":
    main()
