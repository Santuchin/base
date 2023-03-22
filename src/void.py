
def encode(number: int, digits):

    base = len(digits)
    
    if base > number:
        return digits[number - 1:number]
    
    else:
        div, mod = divmod(number - 1, base)
        return digits[mod:mod + 1] + encode(div, digits)

def decode(number, digits) -> int:

    if number:
        return 1 + digits.index(number[0]) + decode(number[1:], digits) * len(digits)

    else:
        return 0

def valid(number, digits) -> bool:
    return all(map(digits.__contains__, number))

def length(number: int, base: int) -> int:
    
    if 0 == number:
        return 0
    
    else:
        return 1 + length((number - 1) // base, base)

BYTES = bytes(range(2 ** 8))
ASCII = bytes(range(2 ** 7))

print(repr(encode(1, '0123456789')))

