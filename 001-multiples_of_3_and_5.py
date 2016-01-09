#!/usr/bin/python3

import 
INTERVAL_END = 1000000


# The straightforward way
def mul_of_3_and_5(start: int, end: int):
    num = start
    while num <= end:
        if num % 3 == 0:
            yield num
        elif num % 5 == 0:
            yield num
        num += 1

l = list(mul_of_3_and_5(1,INTERVAL_END))
#print(l)
a = sum(l)
print(a)

import math as m

# A more clever way using arithmetic progressions
def sum_of_multiples(mult: int, end: int):
    end_sum = m.floor(end / mult)

    sumsum = (end_sum+1)*end_sum/2;

    return sumsum * mult

b = sum_of_multiples(5,INTERVAL_END) + sum_of_multiples(3,INTERVAL_END) - sum_of_multiples(15,INTERVAL_END)

print(b)

assert(int(a) == int(b))


