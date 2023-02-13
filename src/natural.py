
def encode(number: int, digits: str | bytes) -> str | bytes:

    base = len(digits)
    
    if base > number:
        return digits[number:number + 1]
    
    else:
        div, mod = divmod(number, base)
        return encode(div, digits) + digits[mod:mod + 1]

def decode(number: str | bytes, digits: str | bytes) -> int:

    if 1 == len(number):
        return digits.index(number)
    
    else:
        return decode(number[:-1], digits) * len(digits) + digits.index(number[-1])

def valid(number: str | bytes, digits: str | bytes, leading: bool=False) -> bool:

    if number:
        return (True if leading else not number.startswith(digits[0:1])) and all(map(digits.__contains__, number))

    else:
        return False

def length(number: int, base: int) -> int:

    if base > number:
        return 1

    else:
        return 1 + length(number // base, base)

def encode_limited(number: int, digits: str | bytes, length: int) -> str | bytes:

    if 0 == length:
        return type(digits)()
    
    else:

        base = len(digits)
        mod = number % base

        return encode_limited(number // base, digits, length - 1) + digits[mod:mod + 1]

BINARY = '01'
OCTAL = '01234567'
DECIMAL = '0123456789'
HEXADECIMAL = '0123456789abcdef'
BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

