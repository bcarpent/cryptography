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
