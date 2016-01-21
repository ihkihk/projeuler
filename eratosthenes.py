import numpy as np
import math


def eratosthenes(N):
    """Find all prime numbers <= N.

    >>> eratosthenes(1)
    Traceback (most recent call last):
        ...
        assert N >= 2
    AssertionError

    >>> eratosthenes(2)
    array([2])

    >>> eratosthenes(3)
    array([2, 3])

    >>> eratosthenes(4)
    array([2, 3])

    >>> eratosthenes(5)
    array([2, 3, 5])

    >>> eratosthenes(16)
    array([ 2,  3,  5,  7, 11, 13])

    >>> eratosthenes(20)
    array([ 2,  3,  5,  7, 11, 13, 17, 19])

    >>> eratosthenes(23)
    array([ 2,  3,  5,  7, 11, 13, 17, 19, 23])
    """

    assert N >= 2
    primes = np.arange(3, N+1, 2)

    sievestop = int(math.sqrt(N))
    if sievestop % 2 == 0:
        sievestop -= 1

    if N > 3:
        for i in np.arange(3, sievestop+1, 2):
            n = i
            while n <= N-2*i:
                n += 2*i
                primes[int(n/2)-1] = 0

    return np.concatenate(([2], primes[primes != 0]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

