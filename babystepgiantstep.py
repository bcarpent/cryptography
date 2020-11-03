#!/usr/bin/env python3

import fastexponent
import math
import primitiverootsearch

def babyStepGiantStep(base, a, n):

    # Initialization
    result = 0

    # Set b to the base input at command line
    b = base

    # Compute m = ceiling of sqrt(n-1)
    m = int(math.ceil(math.sqrt(n-1)))
    print('m = ', m)

    # BABY STEPS
    # Compute b^j mod n using fast exponentiation for 0 <= j < m
    # Use a dictionary to store the results of the baby steps
    # Initialize first entry in table to (1, 0) for (key, value),
    # where key is the result of fastexponent and value is j.
    babyStepTable = dict()
    babyStepTable = {}
    babyStepTable.setdefault(1, 0)
    j = 1
    while j < m:
        result = fastexponent.calculate(b, j, n)
        babyStepTable.setdefault(result, j)
        j += 1

    print('Baby Step table:', babyStepTable)

    # GIANT STEPS
    # Compute constant c = b^-m
    # Since b is a generator, b^(n-1) = 1 mod n
    # Then b^-m = b^(n-1) * b^-m
    # Thus our exponent for fast exponentiation will be (n-1-m)
    exp = n - 1 - m
    c = fastexponent.calculate(b, exp, n)

    print('Constant c = ', c)

    # Loop through the giant steps in (im) increments
    # First value will be as follows:
    # x0 = a * c^0 = a
    # Lookup result x in babyStepTable for a match
    i = 0
    log = 0
    x0 = a
    if a in babyStepTable:
        j = babyStepTable[a]
        print('We have a match for i = ', i, ', j = ', j)
        log = i * m + j
        if log > (n-1):
            log = log - (n - 1)
        return log

    i = 1
    x = x0
    while i < m:
        x = (x * c) % n
#        print 'i = ', i, ': x = ', x
        if x in babyStepTable:
        	j = babyStepTable[x]
        	print('We have a match for i = ', i, ', j = ', j)
        	log = i * m + j
        	if log > (n-1):
        	    log = log - (n - 1)
        	break
        else:
        	i += 1


    return log

def main():
    print('BABY-STEP GIANT-STEP ALGORITHM')
    print('Compute log base b of a in Z(n)')

    base = int(input("Enter log base: "))
    a = int(input("Enter a: "))
    n = int(input("Enter modulus n: "))

    print

    log = babyStepGiantStep(base, a, n)

    print ('Log result = ', log)


if __name__ == '__main__':
    main()
