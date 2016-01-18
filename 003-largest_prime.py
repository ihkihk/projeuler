#!/usr/bin/python3

import math
import numpy as np

def sieve(N):
    """Perform Eratosthenes sieve to find prime factors of N."""

    maxn = math.sqrt(N)

    factors = np.ones(maxn)

    for i in range(2, len(factors)):
        p = i
        while p < len(factors)-i:
            p += i
            factors[p] = 0

    return np.where(factors==1)[0]


N = 600851475143
factors = sieve(N)

print(factors)

for i in range(len(factors)-1,0,-1):
    if N % factors[i] == 0:
        print(factors[i])
        break

