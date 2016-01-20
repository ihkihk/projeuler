#!/usr/bin/python3

from eratosthenes import eratosthenes

primes = eratosthenes(150000)

if len(primes) < 10001:
    print("Not enough primes")
    exit(1)

print(primes[10000])
