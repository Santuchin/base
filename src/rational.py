from . import natural

def encode(number: tuple[int, int], digits) -> tuple:

    num, den = number

    base = len(digits)
    
    nat, mod = divmod(num, den)

    ratper = digits[0:0]
    mods = {}
    
    index = 0

    while mod and not mod in mods:
    
        mods[mod] = index

        div, mod = divmod(mod * base, den)
        ratper += digits[div:div + 1]

        index += 1

    if mod:
        rat = ratper[:mods[mod]]
        per = ratper[mods[mod]:]

    else:
        rat = ratper
        per = digits[0:0]

    return (natural.encode(nat, digits), rat, per)

def decode(number: tuple, digits) -> tuple[int, int]:
    
    nat, rat, per = number

    base = len(digits)


    ratlen = len(rat)

    if ratlen:
        ratnum = natural.decode(rat, digits)

    else:
        ratnum = 0
    
    pernum = natural.decode(per, digits)

    if pernum:

        perden = base ** len(per) - 1

        ratden = base ** ratlen
    
    else:
    
        perden = 1
        
        if ratnum:
            ratden = base ** ratlen

        else:
            ratden = 1

    num = ratnum * perden + pernum
    den = ratden * perden

    return (natural.decode(nat, digits) * den + num, den)

def reduce(number: tuple[int, int]) -> tuple[int, int]:
    ...

def period(number: tuple[int, int], base: int) -> bool:
    ...


