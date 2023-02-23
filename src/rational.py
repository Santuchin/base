import math

import natural # from . import natural

def log(num, base):

    if base > num:
        return (0, num)

    else:
        div, mod = divmod(num, base)
        res, rem = log(div, base)
        res += 1

        return (res, num - base ** res)

def encode(number: tuple, digits) -> tuple:
    
    num, den = number

    base = len(digits)
    
    nat, mod = divmod(num, den)

    length, rem = log(den, base)

    x = math.lcm(den, base, base - 1) // den
    
    den *= x
    mod *= x

    if 0 == rem:
        rat = natural.encode_limited(mod, digits, length)
        per = digits[0:1]

    else:
        rat = ...
        per = ...

    return (natural.encode(nat, digits), rat, per)

print(encode((1, 3), '0123456789'))













def decode(number: tuple, digits) -> tuple:
    
    nat, rat, per = number

    base = len(digits)


    ratlen = len(rat)

    if ratlen:
        ratnum = natural.decode(rat, digits)

    else:
        ratnum = 0
    
    ratden = base ** ratlen


    pernum = natural.decode(per, digits)

    if pernum:
        perden = base ** len(per) - 1

    else:
        perden = 0


    num = ratnum * perden + pernum
    den = ratden * perden

    return (natural.decode(nat, digits) * den + num, den)

def isper(number: tuple, base: int) -> bool:
    ...

