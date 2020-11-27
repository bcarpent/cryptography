#!/usr/bin/env python3

import euclidean
import math
import miller_rabin
import secrets

def selectPrime():
    primeSelected = False
    while (primeSelected == False):
        # Guess a large prime number
        guess = secrets.choice(range(100000, 500000))
        if guess % 2 != 0:                                # Don't bother with even numbers
            prime = miller_rabin.millerRabinTest(guess, 5)
        else:
            continue

        # Prime candidate must be congruent to 3 mod 4
        if (prime % 4 == 3):
            primeSelected = True

    return prime


def totalBits(number):
    # Convert number to binary and remove first two characters 0b
    binary = bin(number)[2:]
    return len(binary)


def produceRandomInteger(high):
    # How many bits of randomness are needed for the high number?
    num_bits = totalBits(high)
    print('\nTotal bits needed:', num_bits)

    # 1. Use Miller-Rabin to choose two strong pseudoprimes p and q in 5 rounds each
    p = selectPrime()
    q = selectPrime()
    print('\nPrime p:', p)
    print('Prime q:', q)

    # 2. Compute n = p * q
    n = p * q
    print('Modulus n:', n)

    # 3. Randomly choose a seed s0 in multiplicative group Z(n)*
    seedSelected = False
    while (seedSelected == False):
        seed = secrets.choice(range(3, n-1))

        # The seed must be a coprime of n to be in Z(n)*
        gcd = euclidean.euclidean(seed, n)
        if gcd == 1:
            print ('Seed selected: ', seed)
            seedSelected = True

    # Produce sequence of random bits by continually squaring
    s0 = seed
    s1 = (s0 ** 2) % n
    b1 = s1 % 2
    number = b1
    print ('Random bit', 1, ':', b1)
    print ('Random bit sequence:', bin(number))
    for i in range(1, num_bits):
        s2 = (s1 ** 2) % n
        b2 = s2 % 2
        print ('Random bit', i+1, ':', b2)
        number = (b2 << i) + b1

        # Final number must be less than the ceiling passed in as argument
        if (number > high):
            return b1

        print ('Random bit sequence:', bin(number))
        s1 = s2
        b1 = number

    return number


def main():
    print('BLUM-BLUM-SHUB PRNG')
    print('Random Number Generator')

    high = int(input("Enter maximum value: "))

    result = produceRandomInteger(high)

    print ('Blum-Blum-Shub random number: ', result)


if __name__ == '__main__':
    main()
