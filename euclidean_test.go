package main

import (
	"fmt"
	testing "testing"
)

func TestExtendedEuclidean(t *testing.T) {
	var gcd, x0, y0 int

	fmt.Println("Testing extended euclidian algorithnm")

	gcd, x0, y0 = ExtendedEuclidean(161, 28)
	if gcd != 7 {
		t.Error("\nFailed to calculate gcd(161, 28) using extended Euclidean")
	}

	if ((x0 != -1) && (y0 != 6)) {
		t.Error("\nFailed to calculate x0 and y0 for gcd(161, 28) using extended Euclidean")
	}

	gcd, x0, y0 = ExtendedEuclidean(103927, 102313)
	if gcd != 1 {
		t.Error("\nFailed to calculate gcd(102313, 103927) using extended Euclidean")
	}

	if ((x0 != -39239) && (y0 != 39858)) {
		t.Error("\nFailed to calculate x0 and y0 for gcd(102313, 103927) using extended Euclidean")		
	}
}

func TestEuclidean(t *testing.T) {
	var gcd int

	fmt.Println("Testing euclidian algorithnm")

	gcd = Euclidean(36, 10)
	if gcd != 2 {
		t.Error("\nFailed to calculate gcd(36, 10)")
	}

	gcd = Euclidean(2740, 1760)
	if gcd != 20 {
		t.Error("\nFailed to calculate gcd(2740, 1760) using Euclidean")
	}
}