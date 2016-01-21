#!/usr/bin/python3

from factor import factor
from collections import Counter


n = 10000
factors_last = factor(n)
while True:
    n += 1
    factors_n = factors_last
    factors_n1 = factor(n+1)
    factors_last = factors_n1
    factors_triangular = Counter(factors_n) #+ factors_n1
    factors_triangular += Counter(factors_n1)
    factors_triangular[2] -= 1 # simulate dividing by 2
    # Get the factor exponents
    exp = factors_triangular.values()
    num_divisors = 1
    for i in exp:
        num_divisors *= int(i)+1
    if num_divisors >= 500:
        triangular = (n+1)*n/2
        print(triangular)
        print(factors_triangular)
        break


