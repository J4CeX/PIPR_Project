# from space import Space
# from PIL import (
#     Image,
#     ImageDraw
# )
# from objects import (
#     OrbitalObject,
#     CentralObject
# )
import os


def menu_print(width):
    print('*' * width)
    print('SYMULACJA RUCHU W POLU GRAWITACYJNYM'.center(width))
    print('*' * width)
    print('Opcje:')
    print('1. Symulacja')
    print('0. Zakończ')


def simulate():
    print('Obiekt Centralny')
    print('Średnica:')
    diameter = input('>> ')
    print('Masa:')
    mass = input('>> ')


def main():
    width = 40
    while True:
        os.system('cls')
        menu_print(width)
        option = input('>> ')
        if option == '1':
            simulate()
        elif option == '0':
            print("Koniec")
            return


if __name__ == "__main__":
    main()
