import math
from collections import defaultdict
from eratosthenes import eratosthenes


def factor(N):
    """Factor a integer number N.

    >>> factor(1)
    defaultdict(<class 'int'>, {1: 1})

    >>> factor(2)
    defaultdict(<class 'int'>, {2: 1})

    >>> factor(4)
    defaultdict(<class 'int'>, {2: 2})

    >>> factor(41)
    defaultdict(<class 'int'>, {41: 1})

    >>> factor(38556)
    defaultdict(<class 'int'>, {17: 1, 2: 2, 3: 4, 7: 1})

    >>> factor(1307674368000)
    defaultdict(<class 'int'>, {17: 1, 2: 2, 3: 4, 7: 1})
    """
    sqrt_n = int(math.sqrt(N))
    factors = defaultdict(int)

    if N == 1:
        factors[1] = 1
        return factors

    # Find the primes that can be factors
    primes = eratosthenes(N)
    canstop = False
    for p in primes:
        while N % p == 0:
            factors[p] += 1
            N /= p
            if p > sqrt_n:
                canstop = True
        if canstop:
            break

    return factors


if __name__ == "__main__":
    import doctest
    doctest.testmod()

