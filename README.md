# CS 789 Cryptography Final Project

This is a Python library for testing RSA and ElGamal algorithms

## Installation

Download Python here:
https://www.python.org/downloads/

Tested using Python 2.7 and 3.7

```
$ python --version
Python 2.7.16

$ python3 --version
Python 3.7.1
```

## RSA

Bob creates public key, sends over email to Alice, waits for encrypted msg and decrypts
```
$ python ./rsa_decrypt.py
```

Alice encrypts msg and sends to Bob via email
```
$ python ./rsa_encrypt.py
```

Eve factors modulus n and decrypts msg
```
$ python ./rsa_eavesdrop.py
```

## ElGamal

Bob creates public key, sends over email to Alice, waits for encrypted msg and decrypts
```
$ python ./elgamal_decrypt.py
```

Alice encrypts msg and sends to Bob via email
```
$ python ./elgamal_encrypt.py
```

Eve computes log from public key and decrypts msg
```
$ python ./elgamal_eavesdrop.py
```

## Unit Tests

Exercise individual tests as follows.
```
$ python -m unittest -v test_rsa
$ python -m unittest -v test_elgamal
$ python -m unittest -v test_babystepgiantstep
$ python -m unittest -v test_euclidean
$ python -m unittest -v test_fastexponent
$ python -m unittest -v test_miller_rabin
$ python -m unittest -v test_primitiverootsearch
$ python -m unittest -v test_pollards
```

Run the entire test suite as follows.
```
$ python -m unittest discover -v
```

## Text Exchanges

### RSA

#### Bob computes and publishes public key

Bob generates two 20-bit probable primes using Miller-Rabin to form the modulus, computes an encryption and decryption exponent, publishes the public key (via email), and then waits for the encrypted message.

```
$ python ./rsa_decrypt.py
RSA DECRYPTION ALGORITHM
Compute a public key, send to peer, then decrypt incoming message

Strong pseudoprime found: 658913
Strong pseudoprime found: 853159
Prime p found: 658913
Prime q found: 853159
RSA modulus: 562157556167
Order of group: 562156044096
Encryption exponent: 5
Decryption exponent: 449724835277
Send public key (n, e): (562157556167, 5)
Enter peer email address: bcarpent@bu.edu

Public Key (n, e): (562157556167,5)
Opening connection to the server...

Wait for encrypted message to be received...
Enter encrypted message E_x: 
```

#### Alice encrypts a message
```

RSA ENCRYPTION ALGORITHM
Encrypt and send a message x using peer public key (n, e)

Enter group order n:562157556167
Enter encryption exponent e:5
Enter integer message x: 7979123
Encrypted message: 7979123 ^ 5 mod 562157556167 = 117538171076

Enter recipient email address: bcarpent@bu.edu

Encrypted msg x = 117538171076
Opening connection to the server...
Sent encrypted message!
```

#### Bob decrypts the message

When Bob receives the encrypted message from Alice, he decrypts it using his private decryption key.

```
Wait for encrypted message to be received...
Enter encrypted message E_x: 117538171076

Decrypted message: 7979123
```

#### Eve eavesdrops and decrypts the message

From the public key above, Eve uses Pollard's Rho to find a factor of the modulus n. From the two primes and the encryption exponent, she can compute the decryption key and decrypt the encrypted message.

```
$ python ./rsa_eavesdrop.py
RSA EAVESDROPPING
Eve eavesdrops on Alice and Bob. From the public key, decrypt the message
From public key, enter modulus n:562157556167
From public key, enter exponent e:5

Pollards Rho found a factor of 562157556167: 658913
Pollards Rho method factored 562157556167 into p = 658913, q = 853159
Decryption key: 449724835277

Eavesdrop for encrypted message...
Enter encrypted message E_x: 117538171076
Decrypted message: 117538171076 ^ 449724835277 mod 562157556167 = 7979123

Decrypted message: 7979123

```



