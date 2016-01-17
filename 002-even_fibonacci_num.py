#!/usr/bin/python3

def get_fibo():
    n2 = 1
    n1 = 1

    while n2 < 4000000:
        yield n2
        n2, n1 = n1, n1+n2

print(list(get_fibo()))

