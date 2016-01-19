import numpy as np
import math

def eratosthenes(N):
    """Find all prime numbers up to and including N"""

    assert N >= 2
    primes = np.ones(N+1)

    last_prime_to_sieve = int(math.sqrt(N))

    # Kill the initial 0 and 1
    primes[0:2] = 0

    if N > 3:
       
        # Kill all multiples of 2
        np.put(primes, np.arange(4, N+1, 2), 0)

        for i in np.arange(3, last_prime_to_sieve+1):
            n = i
            while n <= N-i:
                n += i
                primes[n] = 0


    return np.where(primes == 1)[0]


gg = eratosthenes(147)
print(gg)

