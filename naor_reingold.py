#!/usr/bin/env python3

import euclidean
import fastexponent
import math
import miller_rabin
import primitiverootsearch
import random
#import secrets

def selectPrime(n):
    primeSelected = False
    while (primeSelected == False):
        # Guess a very large prime number of n bits
        guess = random.SystemRandom().getrandbits(n)
#        guess = secrets.randbits(n)
        if guess % 2 != 0:                                # Don't bother with even numbers
            prime = miller_rabin.millerRabinTest(guess, 5)
            print('Prime candidate found: %d' % prime)
        else:
            continue

        if (prime != 0):
            primeSelected = True

    return prime


def decimalToBinaryArray(x_dec, n):
    # Convert to binary
    x_bin  = bin(x_dec)[2:]

    # Determine pad of leading zeroes
    length = len(x_bin)
    pad = n - length

    # Initialize array of fixed size n to all zeroes
    x = [0] * n

    # Fill in values from the binary value of x starting from pad to end
    j = 0
    for i in range(pad, n):
        x[i] = int(x_bin[j])
        j += 1

    return x


def generateRandomBit(n, N, a, g, r):
    # 7. Choose x which fits within n bits and create array to store binary digits
    x_dec = random.SystemRandom().getrandbits(n)
#    x_dec = secrets.randbits(n)
    x = decimalToBinaryArray(x_dec, n)

    # 8. Compute an exponent based on following formula:
    #    e = a(1, x1) + a(2, x2) + ... + a(n, xn)
    e = 0
    for i in range(0, n):
        e = e + a[i][x[i]]
    print('Exponent e: %d' % e)

    # 9. Compute y = g^e mod N
    y = fastexponent.calculate(g, e, N)

    # 10. Pad B(y) which is 2n bits
    B = decimalToBinaryArray(y, 2 * n)

    # 11. Compute f(x) = r * B(y) mod 2 to generate one bit
    f = 0
    for i in range(0, 2 * n):
        f = f + (r[i] * B[i])

    return f % 2

def rand(low, high):
    # 1. Fix number of bits n to 8
    n = 8
    print('\nFixed n (prime # bits): %d' % n)

    # 2. Randomly generate prime numbers p and q of n bits each
    p = selectPrime(n)
    q = selectPrime(n)
    print('Primes selected: p = %d and q = %d' %(p, q))

    # 3. Compute N = p * q
    N = p * q
    print('Modulus N = %d' % N)

    # 4. Chooose 2n random integers in range 1 < a < N
    #    Use a multidimensional array and initialize first pair to (0,0)
    #    which will be unused. Our first pair will be a[1][0] and a[1][1].
    a = []
    for i in range(0, n):
#        a0 = secrets.choice(range(1, N))
#        a1 = secrets.choice(range(1, N))
        a0 = random.SystemRandom().randint(1, N)
        a1 = random.SystemRandom().randint(1, N)
        a.append([a0, a1])
    print('Multidimensional array a: ', a)

    # 5. Choose a random g, a member of multiplicative group Z(N)* such that
    #    g is a square in Z(N)*
    foundSquare = False
    while (foundSquare == False):
	    b = random.SystemRandom().randint(2, N)
	    gcd = euclidean.gcd(b, N)
	    if gcd == 1:
	        g = (b ** 2) % N
	        gcd2 = euclidean.gcd(g, N)
	        if gcd2 == 1:
	            root = primitiverootsearch.rootSearch(N, g)
	            if (root == g):
	                print('Found a square g', g, 'in Z(', N, ')')
	                foundSquare = True

    # 6. Choose a random r that is 2n bits long and convert to array
    r_dec = random.SystemRandom().getrandbits(2 * n)
    print('Random number r: %d' % r_dec)
    r = decimalToBinaryArray(r_dec, 2 * n)

    # Generate random bit sequence
    num_bits = high.bit_length()
    print('Total bits needed for high value: %d' % num_bits)
    print('\nINITIALIZATION COMPLETE')

    b0 = generateRandomBit(n, N, a, g, r)
    number = b0
    for i in range(1, num_bits):
        b1 = generateRandomBit(n, N, a, g, r)
        number = (b1 << i) + b0

        # Final number must be less than the ceiling passed in as argument
        if (number > high):
            return b0

        b0 = number

    print ('Random number: %d' % number)
    return number


def main():
    print('NAOR-REINGOLD PRNG')
    print('Random Number Generator')

    low  = int(input("Enter minimum value: "))
    high = int(input("Enter maximum value: "))

    result = rand(low, high)

    print ('\nNaor-Reingold random number: %d' % result)


if __name__ == '__main__':
    main()
