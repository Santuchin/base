from . import natural

def encode(number: tuple[int, int], digits) -> tuple:

    num, den = number

    base = len(digits)
    
    nat, rem = divmod(num, den)

    rat = ''
    rem_map = {}
    
    while rem and rem not in rem_map:
    
        rem_map[rem] = len(rat)

        div, rem = divmod(rem * base, den)
        rat += natural.encode(div, digits)

    print(rem_map)

    if rem:
        return (natural.encode(nat, digits), rat[:rem_map[rem]], rat[rem_map[rem]:])

    else:
        return (natural.encode(nat, digits), rat, digits[0:0])

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


