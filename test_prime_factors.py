from unittest import TestCase

def prime_factors_of(number):

    factors = []

    if number < 2:
        return []

    for primes in range (2, number + 1):
        while number % primes == 0:
            factors.append(primes)
            number /= primes

    return factors

class TestPrimeFactors(TestCase):
    def test_0(self):
        self.assertEqual(prime_factors_of(0), [])

    def test_1(self):
        self.assertEqual(prime_factors_of(1), [])

    def test_2(self):
        self.assertEqual(prime_factors_of(2), [2])

    def test_3(self):
        self.assertEqual(prime_factors_of(3), [3])

    def test_4(self):
        self.assertEqual(prime_factors_of(4), [2, 2])

    def test_5(self):
        self.assertEqual(prime_factors_of(5), [5])

    def test_8(self):
        self.assertEqual(prime_factors_of(8), [2, 2, 2])

    def test_large_number(self):
        self.assertEqual(prime_factors_of(2 * 3 * 5 * 17 * 19), [2, 3, 5, 17, 19])
