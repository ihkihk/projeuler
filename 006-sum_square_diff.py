#!/usr/bin/python3

import numpy as np

N = 100

a = np.arange(N+1)

sum_squares = np.sum(a*a)
square_sum = np.sum(a)**2

diff = square_sum - sum_squares
print(a)
print(a*a)
print(sum_squares)
print(square_sum)
print(diff)

