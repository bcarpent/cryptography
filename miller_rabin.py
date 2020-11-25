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


def testRound(n, s, m, b):
    # First compute b0 = b^m mod n
    # If the result is 1 or -1, n is a strong pseudoprime
    print('Base selected:', b)
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
            print('Composite')
            return 0
        elif (b1 == n-1):            # n is a strong pseudoprime
            print('Probable prime')
            return n
        else:                       # continue
            b0 = b1

    # For all s, b1 != -1 so n is definitely a composite
    return 0


# Returns 0 if definitely a composite, or a nonzero n
# if a probable prime
def millerRabinTest(guess, rounds):
    n = 0

    # Any guess must be an odd integer. If not, print error and return.
    if guess != 0 and guess % 2 == 0:
        print('\nYou entered an even number. Please try again with an odd guess greater than 2.')
        return 0

    # If the guess is 0, we continue selecting candidates until we
    # find a prime number.
    searchComplete = False
    n = selectCandidate(guess)
    while (searchComplete == False):
        # Calculate constants s and m such that
        # n - 1 = 2^s * m
        s, m = calculateConstants(n)

        # Start with base b = 2 for the first round. For subsequuent
        # rounds, select random base b such that 1 < b < n - 1.
        # If any round returns 0, it is definitely a composite so we
        # can return 0 if there was a nonzero guess by the user.
        b = 2
        for j in range(rounds):
            print ('\nRound', j + 1)
            result = testRound(n, s, m, b)
            if guess != 0 and result == 0:          # if guess was a composite, return immediately
                return 0
            elif guess == 0 and result == 0:        # if composite and no guess, break and try new n
            	break
            else:                                   # if n is a probable prime, go another round
                b = random.randint(2, n-1)

        # If we found a probable prime after running through all the rounds
        # our search for a prime is complete. Otherwise, try the test with
        # another value of n.
        if result != 0:
            print ('Strong pseudoprime found:', result, 'in', rounds, 'rounds')
            searchComplete = True
        else:
            print ('Integer ', n, 'is definitely a composite, seeking new candidate.')
            n = selectCandidate(0)

    return n


def main():
    print('MILLER RABIN TEST')
    print('Probabilistic Primality Test')

    guess = int(input("Enter odd integer guess or 0 to find a strong pseudoprime: "))
    rounds = int(input("Enter number of rounds to run on probable primes: "))

    # Execute the primality test which returns p and # of rounds
    # If result is 0, the input guess is determined to be a composite. Otherwise the test
    # considers it a strong pseudoprime
    result = millerRabinTest(guess, rounds)

    if result == 0:
        if guess > 0:
            print ('The integer', guess, 'is definitely a composite (not a prime)')
        else:
            print ('No prime found in', rounds, 'number of rounds')
    else:
        print ('Strong pseudoprime found:', result, 'in', rounds, 'rounds')


if __name__ == '__main__':
    main()
