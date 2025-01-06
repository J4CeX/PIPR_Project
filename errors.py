class ValueIsNotFloatError(Exception):
    def __init__(self, value):
        msg = f'Value has to be float ({value})'
        super().__init__(msg)


class ValueIsNotPositiveError(Exception):
    def __init__(self, value):
        msg = f'Value has to be positive ({value})'
        super().__init__(msg)


class ValueIsNotIntegerError(Exception):
    def __init__(self, value):
        msg = f'Value has to be integer ({value})'
        super().__init__(msg)


class RGBValueError(Exception):
    def __init__(self, value):
        msg = f'Value has to be int between [0;255] ({value})'
        super().__init__(msg)


class ValueIsNotStrError(Exception):
    def __init__(self, value):
        msg = f'Value has to be str ({value})'
        super().__init__(msg)
