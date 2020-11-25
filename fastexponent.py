#!/usr/bin/env python3

import math

# Calculate x^e mod n in log(e) time
def calculate(x, e, n):

    # Initialize to (base, exponent, results) for (x, e, y) values
    x1 = x
    e1 = e
    y1 = 1
    y2 = 0

#    print('X: ', x1, ', E: ', e1, ', Y: ', y1, 'for modulus n =', n)

	# If e is even, square x mod n and halve e, no result
	# If e is odd, update the result y = xy mod n and decrement e
	# When e reaches 0, the algorithm is complete, take the latest result y
    while (e1 > 0):
        if e1 % 2 == 0:            # e is EVEN
            x2 = (x1 ** 2) % n
            e2 = e1 / 2
            y2 = y1
        else:                      # e is ODD
            x2 = x1
            e2 = e1 - 1
            y2 = (x1 * y1) % n     # Intermediate result

        # Debug
#        print('X: ', x2, ', E: ', e2, ', Y: ', y2)

        # Update values
        x1 = x2
        e1 = e2
        y1 = y2

    # Final result will be the latest updated result y2
    return y2


def main():
    print('Fast Exponentiation Algorithm')
    print('Compute x^e mod n')
    print

    x = input("Enter integer base x: ")
    e = input("Enter integer exponent e: ")
    n = input('Enter integer modulus n: ')
    print

    x = int(x)
    e = int(e)
    n = int(n)

    result = calculate(x, e, n)
    print('Result: ', x, '^', e, 'mod', n, '=', result)


if __name__ == '__main__':
    main()
