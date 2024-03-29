#!/usr/bin/env python3

import math
import fastexponent
import euclidean
import miller_rabin
import smtplib
from getpass import getpass

def computeGroupOrder(p, q):

    # Given p and q are primes, then the order using Euler's totient function
    # is (p - 1)(q - 1)
    order = (p - 1) * (q - 1)
    return order


def calculateEncryptionDecryptionKeys(p, q):

    # Get the order of the group given p and q
    n = p * q
    print('')   
    print('RSA modulus: %d' % n)

    # Compute the order of the group
    order = computeGroupOrder(p, q)
    print('Order of group: %d' % order)

    # Now find the exponent e, which must be a coprime
    # of the order of the group. Start with a guess of 3
    # (common encryption exponent).
    e = 3
    expFound = False
    while (expFound == False):
#        print('Try e: ', e)

        # Ensure the exponent guess is relatively prime with the order,
        # i.e. their gcd must be 1. If not, increment e and try again.
        # We can also compute the multiplicative inverse of e in Z*(order)
        # using the Extended Euclidean algorithm
        #
        # x0 * order + y0 * e = gcd
        #
        gcd, x0, y0 = euclidean.extendedEuclidean(order, e)
        if gcd == 1:
            expFound = True
        else:
            expFound = False
            e += 1

    print('Encryption exponent: %d' % e)

    # Per the equation above, y0 is our inverse. If y0 is negative, simply
    # add the order to arrive at the positive integer inverse.
    if y0 < 0:
        d = order + y0
    else:
        d = y0

    print('Decryption exponent: %d' % d)

    return e, d


def sendPublicKey(peerEmail, e, n):

    # Setup sender and receivers (Eve is also listening)
    sender = 'bcarpent@bu.edu'
    receivers = [ peerEmail ]

    # Build the message to send
    publicKeyString = 'Public Key (n, e): (' + str(n) + ',' + str(e) + ')'

    lines = ['From: Bob',
             'To: Alice',
             'Subject: RSA Decryption Test',
             '',
              publicKeyString]

    message = '\n'.join(lines)
    print
    print('Sending Alice:')
    print(message)

    # Open the connection
    print('Opening connection to the server...')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Use dummy gmail account to send to Alice
    gmailUser = 'luna.ripowski'
    gmailPassword = 'AliceVsBob789'
    server.login(gmailUser, gmailPassword)
    server.sendmail(sender, receivers, message)
    server.quit()


def rsaDecryption(E_x, d, n):

    # We now have the encryption exponent. Let's run fast exponentiation on
    # the message x
    result = fastexponent.calculate(E_x, d, n)
    print
    return result


def main():
    print('RSA DECRYPTION ALGORITHM')
    print('Compute a public key, send to peer, then decrypt incoming message')
    print

    # Find two prime numbers p and q using 5 rounds of the Miller Rabin primality test
    p = miller_rabin.millerRabinTest(0, 5)
    q = miller_rabin.millerRabinTest(0, 5)

    print('Prime p found: %d' % p)
    print('Prime q found: %d' % q)

    # Product of the two primes will be our modulus n
    n = p * q

    print

    # Returns the encryption and decryption keys
    e, d = calculateEncryptionDecryptionKeys(p, q)

    print('Send public key (n, e): (%d, %d)' %(n, e))

    # Get peer's email and send the public key
    # Python 3 no longer accepts raw_input so skip this step
    try:
        peerEmail = raw_input("Enter peer email address: ")
        sendPublicKey(peerEmail, e, n)
    except NameError:
        pass

    # Now wait for the encrypted message to be received
    print
    print('Wait for encrypted message to be received...')
    E_x = int(input("Enter encrypted message E_x: "))

    # Now decrypt the message received
    decryptedMsg = rsaDecryption(E_x, d, n)

    print('Decrypted message: %d' % decryptedMsg)


if __name__ == '__main__':
    main()
