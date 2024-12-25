from menu import (
    menu_print,
    new_data,
    load_data
)
import os


def main():
    while True:
        os.system('cls')
        menu_print()
        option = input('>> ')
        if option == '1':
            space = new_data()
            print('Enter steps number: ')
            steps = int(input('>> '))
            space.simulate(steps)
            # wyniki oraz możliwość ich zapisu do pliku
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
