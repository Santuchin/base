import natural

def encode(number: int, digits: str | bytes, *, neg: str | bytes='-', pos: str | bytes='+', zero: bool | None=None) -> str | bytes:

    if 0 == number:
        
        if zero is None:
            return digits[0:1]

        else:
            return (pos if zero else neg) + digits[0:1]

    else:
        return (pos if 0 < number else neg) + natural.encode(abs(number), digits)

def decode(number: str | bytes, digits: str | bytes, *, neg: str | bytes='-', pos: str | bytes='+') -> str | bytes:
    
    if number.startswith(neg):
        return -natural.decode(number[len(neg):], digits)

    elif number.startwith(pos):
        return natural.decode(number[len(pos):], digits)
    
    else:
        return 0

def valid(number: str | bytes, digits: str | bytes, leading: bool=False, *, neg: str | bytes='-', pos: str | bytes='+', zero: bool | None=None) -> bool:
    
    if number.startswith(neg):
        return natural.valid(number[len(neg):], digits, leading)
 
    elif number.startswith(pos):
        return natural.valid(number[len(pos):], digits, leading)
    
    elif zero is None:
        return digits[0:1] == number
    
    else:
        return False

def length(number: int, base: int, *, neg: int=1, pos: int=1, zero: bool | None=None) -> int:
    
    if 0 == number:
        
        if zero is None:
            return 1

        else:
            return 1 + (pos if zero else neg)

    else:
        return (pos if 0 < number else zero) + natural.length(abs(number), base)

