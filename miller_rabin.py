#!/usr/bin/env python3

import fastexponent
import random

def selectCandidate(guess):
    candidateFound = False
    while (candidateFound == False):
        # If guess is 0, user wants us to pick a candidate odd number.
        # So let's pick a random number between 101 and 500,000
        if guess == 0:
            n = random.randint(101, 500000)
        else:
            n = guess

        # Primes greater than 2 must be odd, so try again for even guesses
        r = n % 2
        if r == 0:
            candidateFound = False
        else:
        	candidateFound = True
        	break

    print ('\nCandidate odd integer for testing: ', n)
    return n


def calculateConstants(n):
    # Find the largest power 2^s dividing n-1 such that
    # n - 1 = 2^s * m
    constantsFound = False
    i = 1
    while (constantsFound == False):
        r = (n - 1) % (2 ** i)
        if r == 0:
            i += 1
        else:
            s = i - 1
            m = int((n - 1) / (2 ** s))
            constantsFound = True

    print ('Constants m = ', m, ', s = ', s)
    print ('Computed ', n, '- 1 = 2 ^', s, '*', m)
    return s, m

# Returns 0 if definitely a composite, or a nonzero n
# if a probable prime
def millerRabinTest(guess, rounds):
    # First we need to select a candidate value of n, 
    # the integer we are testing for primality
    n = selectCandidate(guess)

    # Calculate constants s and m such that
    # n - 1 = 2^s * m
    s, m = calculateConstants(n)

    # Now select base b such that 1 < a < n - 1
    # Start with base b = 2
    b = 2

    # Compute b0 = b^m mod n
    # If the result is 1 or -1, n is a strong pseudoprime
    b0 = fastexponent.calculate(b, m, n)
    print ('b 0 =', b0)
    if (b0 == 1 or b0 == n-1):
        return n

    # Previous step did not conclusively determine if n is a
    # composite or prime, so we continue.
    # Loop from 1 to s - 1 and continue squaring resuult and testing
    for i in range(1, s):
        b1 = (b0 ** 2) % n
        print ('b', i, '=', b1)
        if (b1 == 1):                # n is definitely composite
            return 0
        elif (b1 == n-1):            # n is a strong pseudoprime
            return n
        else:                       # continue
            b0 = b1

    # For all s, b1 != -1 so n is definitely a composite
    print('Exhausted all values of s')
    return 0

def main():
    print('MILLER RABIN TEST')
    print('Probabilistic Primality Test')

    guess = int(input("Enter odd integer guess or 0 to find a strong pseudoprime: "))
    rounds = int(input("Enter number of rounds to run the test: "))

    # Execute the primality test which returns p and # of rounds
    # If p = 0, the input guess is determined to be a composite. Otherwise the test
    # considers it a strong pseudoprime
    p = millerRabinTest(guess, rounds)

    if p == 0:
        if guess > 0:
            print ('The integer', guess, 'is definitely a composite (not a prime)')
        else:
            print ('No prime found in', rounds, 'number of rounds')
    else:
        print ('Strong pseudoprime found:', p, 'in', rounds, 'rounds')


if __name__ == '__main__':
    main()
