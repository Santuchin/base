
def encode(number: int, digits: str | bytes) -> str | bytes:

    base = len(digits)
    
    if base > number:
        return digits[number - 1:number]
    
    else:
        div, mod = divmod(number - 1, base)
        return digits[mod:mod + 1] + encode(div, digits)

def decode(number: str | bytes, digits: str | bytes) -> int:

    if number:
        return 1 + digits.index(number[0]) + decode(number[1:], digits) * len(digits)

    else:
        return 0

def valid(number: int, digits: str | bytes) -> bool:
    return all(map(digits.__contains__, number))

def length(number: int, base: int) -> int:
    ...

BYTES = bytes(range(2 ** 8))
ASCII = bytes(range(2 ** 7))

