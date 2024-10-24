
def encode(number: int, digits):

    base = len(digits)
    
    if base > number:
        return digits[number:number + 1]
    
    else:
        div, mod = divmod(number, base)
        return encode(div, digits) + digits[mod:mod + 1]

def decode(number, digits) -> int:

    if 1 == len(number):
        return digits.index(number)
    
    else:
        return decode(number[:-1], digits) * len(digits) + digits.index(number[-1])

def valid(number, digits, leading: bool=False) -> bool:
    return number and all(map(digits.__contains__, number))) and (number == digits[0:1] or (leading or number[0] != digits[0]))

def length(number: int, base: int) -> int:

    if base > number:
        return 1

    else:
        return 1 + length(number // base, base)

def encode_limited(number: int, digits, length: int):

    if 0 == length:
        return digits[0:0]
    
    else:

        base = len(digits)
        div, mod = divmod(number, base)

        return encode_limited(div, digits, length - 1) + digits[mod:mod + 1]

BINARY = '01'
OCTAL = '01234567'
DECIMAL = '0123456789'
HEXADECIMAL = '0123456789abcdef'
BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

