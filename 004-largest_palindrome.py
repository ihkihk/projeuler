#!/usr/bin/python3

import itertools as it

def palindrome(num_digits):
    """Return a sorted list of palindrome numbers of a given size."""

    assert num_digits > 1

    half = int(num_digits / 2)
    upper = it.filterfalse(lambda x: x[0] == '0', it.product("0123456789", repeat=half))

    if num_digits % 2 == 0:
        pal = (u + tuple(reversed(u)) for u in upper)
    else:
        pal = []
        aux = list(upper)
        for i in "0123456789":
            pal.extend(list((u + tuple(i) + tuple(reversed(u)) for u in aux)))

    return sorted(int("".join(y)) for y in pal)

pal = palindrome(6)
print(pal)

for p in reversed(pal[:-2]):
    for d in reversed(range(100, 999)):
        if p % d == 0:
            if p / d > 1000:
                continue
            else:
                print(p)
                print(d)
                exit(1)

