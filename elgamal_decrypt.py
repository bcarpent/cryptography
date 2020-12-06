#!/usr/bin/env python3

import blumblumshub
import euclidean
import fastexponent
import math
import miller_rabin
import primitiverootsearch
import smtplib
from getpass import getpass

def findGenerator(p):
    # Find a primitive root of Z(p)* with initial guesses of 2, 3, and 5
    g = 0
    guess = 2
    while (g == 0):
        g = primitiverootsearch.rootSearch(p, guess)
        if g != 0:
   	        return g
        else:
            guess += 1

        if guess == 4:    # Skip 4 and try 5
            guess = 5
        if guess > 5:     # After 5, let the algorithm pick a random guess
            guess = 0


def computePublicKey(p):
    # Find generator b of Z(p)*
    b = findGenerator(p)

    # Use Blum-Blum-Shub PRNG to choose secret l from {2, ..., p-2}
    l = blumblumshub.rand(2, p-2)

    print('\nBob has secret l: %d' % l)

    # Compute public key b^l % p
    b_l = fastexponent.calculate(b, l, p)

    return b, b_l, l


def decrypt(E_x, b_r, p, l):
    print('Computing (%d)^%d' %(b_r, l))

    # Bob computes (b^r)^l
    b_r_l = fastexponent.calculate(b_r, l, p)

    # Now use the Extended Euclidean algorithm to compute the
    # inverse of (b^r)^l, where
    # GCD (m, n) = (x0)m + (y0)n
    # and the inverse will be x0
    gcd, x0, y0 = euclidean.extendedEuclidean(b_r_l, p)

    # Decryted message x = ((b^r)^l)-1 * E(x)
    plaintext = (x0 * E_x) % p

    return plaintext


def sendPublicKey(peerEmail, p, b, b_l):
    # Setup sender and receivers (Eve is also listening)
    sender = 'bcarpent@bu.edu'
    receivers = [ peerEmail ]

    # Build the message to send
    publicKeyString = 'Public Key (p, b, b_l): (' + str(p) + ',' + str(b) + ',' + str(b_l) + ')'

    lines = ['From: Bob',
             'To: Alice',
             'Subject: ElGamal Public Key',
             '',
              publicKeyString]

    message = '\n'.join(lines)

    # Open the connection
    print('Opening connection to the server...')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Use dummy gmail account to send to Bob
    gmailUser = 'luna.ripowski'
    gmailPassword = 'AliceVsBob789'
    server.login(gmailUser, gmailPassword)
    server.sendmail(sender, receivers, message)
    server.quit()


def main():
    print('ELGAMAL DECRYPTION ALGORITHM')
    print('Generate the Elgamal keys, send to peer, then decrypt incoming message')

    # Find a prime numbers p using 5 rounds of the Miller Rabin primality test
    p = miller_rabin.millerRabinTest(0, 5)
    print('Prime p modulus: %d' % p)

    # Compute the public key
    b, b_l, l = computePublicKey(p)

    print('Sending public key (p, b, b^l): (%d, %d, %d)' %(p, b, b_l))

    # Get peer's email and send the public key
    # Python 3 no longer accepts raw_input so skip this step
    try:
        peerEmail = raw_input("Enter peer email address: ")
        sendPublicKey(peerEmail, e, b, b_l)
    except NameError:
        pass

    # Now wait for the encrypted message to be received
    print
    print('\nNow wait for encrypted message to be received...')
    b_r = int(input("Enter Alice's public key b^r: "))
    E_x = int(input("Enter encrypted message E(x): "))

    # Now decrypt the message received
    decryptedMsg = decrypt(E_x, b_r, p, l)

    print('\nDecrypted plaintext: %d' %decryptedMsg)


if __name__ == '__main__':
    main()
