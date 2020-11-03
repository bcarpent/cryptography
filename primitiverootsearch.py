#!/usr/bin/env python3

import random
import fastexponent

def selectBase(p, root):

    # Common primitive roots: 2, 3, 5
    # Could start with common roots but let's use random b to
    # test more thoroughly.
    if root == 0:
        b = random.randint(2, p-1)
    else:
    	b = root

#    print 'Try with base ', b
    return b


def findPossibleExponents(p):
    expList = []
    factorList = []

    # Initialize remainder and q to 1 and 2, respectively
    r = 1
    q = 2

    # Find a list of potential factors q for every q
    # dividing p-1 (that is, a zero remainder r). Then compute
    # the exponent and add to the list.
    while (q < p):
        r = (p-1) % q
        if r == 0:
#            print 'Found a factor q = ', q
            factorList.append(q)
            exp = (p-1)/q
#            print 'Adding exponent ', exp, ' to list'
            expList.append(exp)

        # Incrememt q and look for another factor
        q += 1

	# Return all list of possible exponents
    return expList, factorList


# Find primitive roots for multiplicative group Z(p)
def rootSearch(p, root):

    # Initialize booleans
    searchComplete = False
    bRejected = False
    attempts = 0

    while (searchComplete == False):
        b = selectBase(p, root)

        expList, factorList = findPossibleExponents(p)
#        print 'Factor list for', p-1, ': ', factorList
#        print 'Exponent list: ', expList
        for exp in expList:
            result = fastexponent.calculate(b, exp, p)
            # If result is 1, this is not a primitive root.
            # Break out of the for loop and start over with a new base
            if result == 1:
                bRejected = True
                break

        # Found a primitive root, return b
        if bRejected:
#            print 'No primitive root found for base = ', b, ", try again with a new base"
            bRejected = False
            attempts += 1

            # If the user guessed a primitive root incorrectly, bail out
            if root > 0:
                searchComplete = True
                b = 0
        else:
        	searchComplete = True

    # Primitive root found, return b
    return b


def main():
    print
    print('PRIMITIVE ROOT SEARCH')
    print('Find a primitive root for multiplicative group Z(p)')

    p = input("Enter prime modulus p: ")
    guess = input("Enter integer root to guess or 0 to loop through random numbers: ")

    p = int(p)
    guess = int(guess)

    # Execute the primitive root search
    root = rootSearch(p, guess)

    print
    if root == 0:
        if guess > 0:
            print ('The integer', guess, 'is not a primitive root for multiplicative group Z(', p, ')')
        else:
            print ('No primitive root found for multiplicative group Z(', p, ')')
    else:
        print ('Primitive root found: ', root)

    print


if __name__ == '__main__':
    main()
