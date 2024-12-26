import os
from space import Space


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


def show_results(space: Space):
    pass
