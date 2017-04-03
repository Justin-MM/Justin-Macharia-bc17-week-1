from unittest import TestCase

from primes_generator import prime_function


class TestPrime(TestCase):
    def test_it_does_not_accept_strings(self):
        with self.assertRaises(ValueError) as context:
            prime_function("30")
            self.assertEqual("The provided input is not an integer!", context.exception.message,
                             "Invalid input of type str is not allowed")

    def test_the_output_is_correct(self):
        self.assertEqual(prime_function(30), [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_it_does_not_accept_zero_as_input(self):
        n = prime_function(0)
        self.assertEqual(n, 'Invalid input', msg='the input should be an integer greater than zero')

    def test_the_output_is_a_list(self):
        self.assertEqual(isinstance(prime_function(30), list), True)

    def test_it_does_not_accept_negatives_as_input(self):
        n = prime_function(-20)
        self.assertEqual(n, 'Invalid input', msg='the input should be an integer greater than zero')