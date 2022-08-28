# Cryptography Project

Author: Brian Carpenter
This is a Python library implementing and testing RSA and ElGamal algorithms

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

### ElGamal

#### Bob computes and publishes public key

Bob finds a prime number using 5 rounds of the Miller Rabin algorithm. Bob computes a generator b of the multiplicative group Z(p). He then uses the Blum-Blum-Shub PRNG to choose a secret l and computes the public key using fast exponentiation.
```
$ python ./elgamal_decrypt.py
ELGAMAL DECRYPTION ALGORITHM
Generate the Elgamal keys, send to peer, then decrypt incoming message
Strong pseudoprime found: 583991
Prime p modulus: 583991

Total bits needed: 20
Strong pseudoprime found: 147779
Strong pseudoprime found: 361003
Prime p: 147779
Prime q: 361003
Modulus n: 53348662337
Random number generated: 334272

Bob has secret l: 334272
Sending public key (p, b, b^l): (583991, 303963, 478436)
Enter peer email address: bcarpent@bu.edu

Now wait for encrypted message to be received...
Enter Alice's public key b^r: 
```

#### Alice encrypts a message

Alice chooses a random secret r using the Blum-Blum-Shub PRNG. Given Bob's public key, she then computes her public key b^r mod p using fast exponentiation. She then encryts a message x = x (b^l)^r. Alice sends her public key and the encrypted message to Bob via email.

```
$ python ./elgamal_encrypt.py
ELGAMAL ENCRYPTION ALGORITHM
Given the public key, encrypt a message and send to peer

Enter public key values
Enter integer prime modulus: 583991
Enter integer generator b: 303963
Enter integer b^l mod p: 478436
Enter integer message x: 123456

Total bits needed: 20
Strong pseudoprime found: 480803
Prime p: 476039
Prime q: 480803
Modulus n: 228880979317
Random number generated: 140068
Alice chooses a secret r: 140068
Alice has public key (b, b^r): (303963, 499328)
Encrypted message: 180223

Sending public key (b^r) = 499328 and encrypted msg E(x) = 180223
Enter recipient email address: bcarpent@bu.edu
Opening connection to the server...
Sent encrypted message!
Sent public key and encrypted message to Bob!
```

#### Bob decrypts the message

From Alice's public key and his secret l, Bob decrypts the message using fast exponentiation and the Extended Euclidean algorithm to compute (b^r)^l, the inverse of (b^r)^l, and finally arrive at x = ((b^r)^l)-1 * E(x).

```
Enter Alice's public key b^r: 499328
Enter encrypted message E(x): 180223
Computing (499328)^334272

Decrypted plaintext: 123456
```

#### Eve eavesdrops and decrypts the message

Eve listens in and finds Bob's secret l, the log base of b of b^l. We use the Baby-Step Giant-Step algorithm to compute the discrete log. From the secret l, Eve can then decrypt the message to arrive at the plaintext message x = ((b^r)^l)-1 * E(x) using fast exponentiation and the Extended Euclidean algorithm.

```
$ python ./elgamal_eavesdrop.py
ELGAMAL EAVESDROPPING ALGORITHM
Eve eavesdrops on Alice and Bob using Baby-Step, Giant-Step Algorithm

From Bob's public key, enter prime modulus p: 583991
From Bob's public key, enter base b: 303963
From Bob's public key, enter b^l: 478436
m = 765

Baby Step table:
(1, ' : ', 0)
(462850, ' : ', 652)
(561155, ' : ', 408)
(92166, ' : ', 144)
(112647, ' : ', 584)
(57489, ' : ', 485)
(31404, ' : ', 728)
(358411, ' : ', 401)
...
(450559, ' : ', 595)
Constant c = 474270
We have a match for i = 436, j = 732

Eve computed secret l = 334272
From Alice's public key, enter b^r: 499328

Enter encrypted message E(x): 180223

Decrypted plaintext: 123456

```

