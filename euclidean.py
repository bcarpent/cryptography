#!/usr/bin/env python3

import math

def gcd(m, n):
	# Process of reduction:
	# We initially calculate the remainder of m / n.
	# We then replace the dividend and divisor each time as follows
	# and update the remainder.
	# When the remainder finally reaches 0, we stop and return the
	# new divisor.
	#
	# GCD(36,10) = GCD(10,6) = GCD(6,4) = GCD(4,2)
	#            = 2
    r = m % n
    divisor = n

    while (r > 0):
        dividend = divisor
        divisor = r
        r = dividend % divisor

    return divisor


def extendedEuclidean(m, n):
    # Initialize r1, r2
    r1 = m
    r2 = n

    # These initialized values are fixed per the algorithm
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while (r2 > 0):
        q = r1 // r2         # quotient

        # Update the r values
        r = r1 - q * r2
        r1 = r2
        r2 = r

        # Update the s values
        s = s1 - q * s2
        s1 = s2
        s2 = s

        # Update the t values
        t = t1 - q * t2
        t1 = t2
        t2 = t

    # GCD (m, n) = (x0)m + (y0)n
    gcd = r1
    x0  = s1
    y0  = t1

    return gcd, x0, y0


def main():
    print('Euclidean and Extended Algorithnms')
    print('Compute GCD(m, n)')

    m = input("Enter integer m: ")
    n = input("Enter integer n: ")

    m = int(m)
    n = int(n)

    # Swap m and n to force m as the larger number
    if n > m:
        temp = m
        m = n
        n = temp

	# Calculate GCD from the Euclidean Algorithm
    print
    print('EUCLIDEAN ALGORITHM')
    gcd = gcd(m, n)
    print('GCD(', m, ',', n, ') = ', gcd)

    print
    print('EXTENDED EUCLIDEAN')
    gcd, x0, y0 = extendedEuclidean(m, n)
    print('GCD(', m, ',', n, ') = ', gcd)
    print('(', x0, ')(', m, ') + (', y0, ')(', n, ') = ', gcd)


if __name__ == '__main__':
    main()
