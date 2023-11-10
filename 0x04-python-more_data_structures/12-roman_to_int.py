#!/usr/bin/python3
def to_subt(list_):
    _sub = 0
    malist = max(list_)

    for n in list_:
        if malist > n:
            _sub += n

    return (malist - _sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_not = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    _keys = list(rom_not.keys())

    n = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in _keys:
            if r_num == ch:
                if rom_not.get(ch) <= last_rom:
                    n += to_subt(list_num)
                    list_num = [rom_not.get(ch)]
                else:
                    list_num.append(rom_not.get(ch))

                last_rom = rom_not.get(ch)

    n += to_subt(list_num)

    return (n)
