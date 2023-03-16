from . import natural

def encode(number: tuple, digits) -> tuple:
    
    num, den = number

    base = len(digits)


    nat, mod = divmod(num, den)
    
    rat = ...
    per = ...

    return (natural.encode(nat, digits), rat, per)

def decode(number: tuple, digits) -> tuple:
    
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

def isper(number: tuple, base: int) -> bool:
    ...


