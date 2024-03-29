#!/usr/bin/env python3

import blumblumshub
import euclidean
import fastexponent
import math
import primitiverootsearch
import smtplib
from getpass import getpass

def encrypt(p, b, b_l, x):
	# Use Blum-Blum-Shub PRNG to choose secret r from {2, ..., p-2}. 
    r = blumblumshub.rand(2, p-2)

    print('Alice chooses a secret r: %d' % r)

    # Compute public key b^r mod p
    b_r = fastexponent.calculate(b, r, p)

    print('Alice has public key (b, b^r): (%d, %d)' %(b, b_r))

    # Compute (b^l)^r mod p
    b_l_r = fastexponent.calculate(b_l, r, p)

    # Encrypted message E_x = x * (b^l)^r
    E_x = (x * b_l_r) % p

    return E_x, b_r


def sendEncryptedMsg(recipientEmail, encryptedMsg):
    # Setup sender and receivers (Eve is also listening)
    sender = 'bcarpent@bu.edu'
    receivers = [ recipientEmail ]

    # Build the message to send
    encryptedMsgString = 'Encrypted msg x = ' + str(encryptedMsg)

    lines = ['From: Alice',
             'To: Bob',
             'Subject: ElGamal Encrypted Msg',
             '',
              encryptedMsgString]

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
    print('ELGAMAL ENCRYPTION ALGORITHM')
    print('Given the public key, encrypt a message and send to peer')
    print

    print('\nEnter public key values')
    p = int(input("Enter integer prime modulus: "))
    b = int(input("Enter integer generator b: "))
    b_l = int(input("Enter integer b^l mod p: "))
    x = int(input("Enter integer message x: "))

    # Plaintext message must be less than prime modulus
    while (x >= p):
        print('\n*** Message must be less than the prime modulus p = %d' % p)
        x = int(input("Enter integer message x < p:"))

    # Encrypt the message with Bob's public key (p, b, b^l)
    encryptedMsg, b_r = encrypt(p, b, b_l, x)

    print('Encrypted message: %d' % encryptedMsg)

    # Send public key and encrypted message to peer
    print('\nSending public key (b^r) = %d and encrypted msg E(x) = %d' %(b_r, encryptedMsg))
    try:
        recipientEmail = raw_input("Enter recipient email address: ")
        sendEncryptedMsg(recipientEmail, encryptedMsg)
        print('Sent encrypted message!')
    except NameError:
        pass
    print('Sent public key and encrypted message to Bob!')

if __name__ == '__main__':
    main()

