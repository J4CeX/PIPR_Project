def int_input(msg=''):
    """
    Takes input data that must be positive integer.
    """
    while True:
        number = input(f'{msg}>> ')
        if number.isdigit():
            number = int(number)
            return number
        else:
            print('It has to be positive int!')


def float_input(msg=''):
    """
    Takes input data that must be float.
    """
    while True:
        number = input(f'{msg}>> ')
        try:
            number = float(number)
        except ValueError:
            print('It has to be float!')
            continue
        else:
            return number


def positive_float_input(msg=''):
    """
    Takes input data that must be positive float.
    """
    while True:
        number = float_input(msg)
        if number > 0:
            return number
        else:
            print('Value has to be positive!')


def RGB_input():
    """
    Takes input data, that must be integers between 0 and 255,
    and converts it to a 3-element tuple of RGB values.
    """
    print('[0;255]')
    while True:
        R = int_input('R: ')
        if R >= 0 and R <= 255:
            break
        else:
            print('It has to be int between [0;255]!')
    while True:
        G = int_input('G: ')
        if G >= 0 and G <= 255:
            break
        else:
            print('It has to be int between [0;255]!')
    while True:
        B = int_input('B: ')
        if B >= 0 and B <= 255:
            break
        else:
            print('It has to be int between [0;255]!')
    return (R, G, B)
