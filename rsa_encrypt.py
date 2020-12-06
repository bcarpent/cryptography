#!/usr/bin/env python3

import math
import fastexponent
import smtplib
from getpass import getpass

def rsaEncryption(n, e, x):
    # We now have the encryption exponent. Let's run fast exponentiation on
    # the message x
    result = fastexponent.calculate(x, e, n)
    print('Encrypted message: %d ^ %d mod %d = %d' %(x, e, n, result))
    print
    return result


def sendEncryptedMsg(recipientEmail, encryptedMsg):
    # Setup sender and receivers (Eve is also listening)
    sender = 'bcarpent@bu.edu'
    receivers = [ recipientEmail ]

    # Build the message to send
    encryptedMsgString = 'Encrypted msg x = ' + str(encryptedMsg)

    lines = ['From: Alice',
             'To: Bob',
             'Subject: RSA Encryption Test',
             '',
              encryptedMsgString]

    message = '\n'.join(lines)
    print
    print('Message to send:')
    print(message)

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
    print('RSA ENCRYPTION ALGORITHM')
    print('Encrypt and send a message x using peer public key (n, e)')
    print

    n = int(input("Enter group order n:"))
    e = int(input("Enter encryption exponent e:"))
    x = int(input("Enter integer message x: "))

    # Plaintext message must be less than prime modulus
    while (x >= n):
        print('\n*** Message must be less than the modulus n = ' % n)
        x = int(input("Enter integer message x < n:"))

    # Encrypt the message x with public key
    encryptedMsg = rsaEncryption(n, e, x)

    # Send public key and encrypted message to peer
    try:
        recipientEmail = raw_input("Enter recipient email address: ")
        sendEncryptedMsg(recipientEmail, encryptedMsg)
        print('Sent encrypted message!')
    except NameError:
        pass


if __name__ == '__main__':
    main()

