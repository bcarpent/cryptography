package main

import (
    "fmt"
//    "math/big"
)

func Euclidean(m int, n int) (int) {
	var dividend int

	/*
	 * Process of reduction:
	 * We initially calculate the remainder of m / n.
	 * We then replace the dividend and divisor each time as follows
	 * and update the remainder.
	 * When the remainder finally reaches 0, we stop and return the
	 * new divisor.
	 *
	 * GCD(36,10) = GCD(10,6) = GCD(6,4) = GCD(4,2)
	 *            = 2
	 */
	r := m % n                    // remainder  = 6
	divisor := n                  // divisor    = 10
	for r > 0  {
		dividend = divisor        // dividend   = 10   6   4
		divisor = r               // divisor    =  6   4   2
		r = dividend % divisor    // remainder  =  4   2   0
	}

	// Our GCD is the last divisor when remainder is 0
	return divisor
}

func ExtendedEuclidean(m int, n int) (gcd int, x0 int, y0 int) {
	var q, r, r1, r2, s, s1, s2, t, t1, t2 int

	// Initialize r1, r2
	r1 = m
	r2 = n

	// These initialized values are fixed per the algorithm
	s1 = 1
	s2 = 0
	t1 = 0
	t2 = 1

	for r2 > 0 {
		q = r1 / r2                 // quotient

		// Update the r values
		r = r1 - q * r2
		r1 = r2
		r2 = r

		// Update the s values
		s = s1 - q * s2
		s1 = s2
		s2 = s

		// Update the t values
		t = t1 - q * t2
		t1 = t2
		t2 = t
	}

	// GCD (m, n) = (x0)m + (y0)n
	gcd = r1
	x0  = s1
	y0  = t1

	return gcd, x0, y0
}

func main() {

	var m, n int

	fmt.Println("Euclidean and Extended Algorithnms")
	fmt.Println("Compute GCD(m, n)")

	fmt.Printf("Enter integer m: ")
	_, err1 := fmt.Scanf("%d", &m)
	if err1 != nil {
		fmt.Println(err1)
		return
	}

	fmt.Printf("Enter integer n: ")
	_, err2 := fmt.Scanf("%d", &n)
	if err2 != nil {
		fmt.Println(err2)
		return
	}

	// Swap m and n to force m as the larger number
	if n > m {
		temp := m
		m = n
		n = temp
	}

	// Calculate GCD from the Euclidean Algorithm
	gcd := Euclidean(m, n)
	fmt.Printf("\nEUCLICEAN ALGORITHM:\n")
	fmt.Printf("GCD (%d, %d) = %d\n", m, n, gcd)

	gcdExt, x0, y0 := ExtendedEuclidean(m, n)
	fmt.Printf("\nEXTENDED EUCLIDEAN ALGORITHM:\n")
	fmt.Printf("GCD (%d, %d) = %d\n", m, n, gcdExt)
	fmt.Printf("x0 = %d, y0 = %d\n", x0, y0)
	fmt.Printf("(%d)(%d) + (%d)(%d) = %d\n", x0, m, y0, n, gcdExt)
}
