#!/usr/bin/python3

import numpy as np
from collections import defaultdict
from factor import factor

lcm_factors = defaultdict(int)
N=20
for i in range(2,N+1):
    f = factor(i)
    for k,v in f.items():
        lcm_factors[k] = max(lcm_factors[k], v)

n = 1
for k,v in lcm_factors.items():
    print(k)
    print(v)
    n *= k**v
    print(n)
        
print(lcm_factors)
print(n)


