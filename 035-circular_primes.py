#!/usr/bin/python3

import itertools as it
from eratosthenes import eratosthenes

def gen_circular(N):
    n_str = str(N)
    if len(n_str) == 1:
        return [N]

    for c in n_str:
        if c in "024568":
            return None

    res = []
    cur = n_str
    for i in range(len(n_str)):
        res.append(int(cur))
        cur = cur[-1] + cur[:-1]

    return res

N = 1000000
primes = eratosthenes(N)
print(len(primes))

assert N > 1
circ_primes = []

for p in primes:
    circulars = gen_circular(p)
    if circulars is None:
        continue
    print(p)
    print(circulars)
    prime_test = list(map(lambda x: x in primes, circulars))
    print(prime_test)
    if all(prime_test):
        circ_primes.append(p)

print(circ_primes)
print(len(circ_primes))


