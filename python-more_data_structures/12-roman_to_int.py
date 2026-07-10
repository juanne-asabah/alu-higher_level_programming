#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string,str) or roman_string is None:return 0
    roman_map = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total = 0
    max_seen = 0
    for char in reversed(roman_string):
        val = roman_map.get(char,0)
        if val >= max_seen:
            total += val
            max_seen = val
        else:total -= val
    return total
