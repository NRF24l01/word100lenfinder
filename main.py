def get_let(let: str) -> int:
    if ord(let) > 1077 and not ord(let) == 1105:
        print(abs(31 - (ord("я")-ord(let)))+2)
    elif ord(let) == 1105:
        print(7)
    else:
        print(abs(31 - (ord("я")-ord(let)))+1)

