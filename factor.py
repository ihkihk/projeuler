
import math
from collections import defaultdict
from eratosthenes import eratosthenes

def factor(N):
    max_factor = int(math.sqrt(N))
    factors = defaultdict(int)

    # Find the primes that can be factors
    primes = eratosthenes(N)
    for p in primes:
        while True:
            if N % p == 0:
                factors[p] += 1
                N /= p
            else:
                break

    return factors

g = factor(123)
print(g)
