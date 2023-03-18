
DIGITS = 'IVXLCDM'
VALUE = {5: 1, 2: 3}

def encode(number: int, digits=DIGITS, value: dict[int: int]=VALUE):
    ...

def decode(number, digits=DIGITS, value: dict[int: int]=VALUE) -> int:
    ...

def valid(number, digits=DIGITS, value: dict[int: int]=VALUE) -> bool:
    ...

def length(number: int, value: dict[int: int]=VALUE) -> int:
    ...

