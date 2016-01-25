#!/usr/bin/python3

import math as m

# Brute force calculation of Champernowne's constant
ch = ""
for i in range(1, 1000000):
    ch += str(i)

ans = 1
for d in (1, 10, 100, 1000, 10000, 100000, 1000000):
    print("Digit #{}: {}".format(d, ch[d-1]))
    ans *= int(ch[d-1])

print(ans)

# Intelligent calculation

# Calculate decade boundaries
# end(0) = 0
# start(d) = end(d-1) + 1
# len(d) = d*(10**d - 10**(d-1)) = 9*d*10**(d-1)
# end(d) = start(d) + len(d) - 1 = end(d-1) + len(d) = sum(len(k), k=1..d) =
#        = 9 * sum(k*10**(k-1), k = 1..d)
#        Which gives for 1<d<9: end(4)=9*4321, end(8)=9*87654321
print("Decade\t\t\tStart\t\t\tLen\t\t\tEnd")
last_endd = 0
for d in range(1, 7):
    startd = last_endd + 1
    lend = d*(10**d - 10**(d-1))
    endd = startd + lend - 1
    last_endd = endd
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(d, startd, lend, endd))


def num2loc(N):
    """Returns the location (1-based) in the Champernownes' constant of the first (leftmost) digit of given number"""
    dec = m.ceil(m.log10(N+1))
    prevdec_id = 0
    if dec > 1:
        for x in range(dec-1):
            prevdec_id += (x+1)*10**x
    print(prevdec_id)
    dec_start = 9*prevdec_id + 1
    num_loc = (N - 10**(dec-1)) * dec + dec_start
    return num_loc

for i in (5, 10, 13, 100, 1000, 999, 1001):
    print("Location of {} in Champernowne's constant: {}".format(i, num2loc(i)))


def loc2num_dig(loc):
    """Returns the number and its digit where a given location (1-based) points in the Champernowne's constant"""
    def lo_dec_bdr(nd):
        """Return the lowest location boundary for locations having nd number of digits"""
        if nd == 1:
            return 1
        if nd == 2:
            return 10
        bdr = []
        bdr.append(str(nd-2))
        bdr.append("8"*(nd-3))
        bdr.append("90")
        nbdr = int("".join(bdr))
        return nbdr

    # In which decade are we
    num_digits = m.floor(m.log10(loc)) + 1
    ldb = lo_dec_bdr(num_digits)
    dec = m.floor(m.log10(ldb)) + 1
    if ldb > loc:
        dec -= 1

    base_loc = num2loc(10**(dec-1))
    # Note: the decade also coincides with the number of digits in the decade's numbers
    num = m.floor((loc - base_loc)/dec + 10**(dec-1))
    dig = str(num)[(loc-base_loc) % dec]
    return (num, dig)


#for i in (5, 16,  230, 2889, 40000,  350000, 38889, 38890, 488889, 488890):
#    print("Location {} is in decade {}".format(i, loc2num_dig(i)))

for i in (5, 16, 17, 18, 1000):
    num, dig = loc2num_dig(i)
    print("Location {} contains the digit {} which belongs to number {}".format(i, dig, num))


ans = 1
for d in (1, 10, 100, 1000, 10000, 100000, 1000000):
    digit = loc2num_dig(d)[1]
    print("Digit #{}: {}".format(d, digit))
    ans *= int(digit)

print(ans)

