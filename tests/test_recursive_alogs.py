import math
import unittest

from algos.recursion import *


class TestLinkedList(unittest.TestCase):

    def test_factorial(self):
        n = 10
        assert math.factorial(n) == compute_factorial(n)

    def test_reverse_string(self):
        s = 'abc'
        assert 'cba' == reverse_string(s)

    def test_print_array(self):
        print_array([1, 2, 3])

    def test_a_power_b(self):
        a = 6
        b = 3
        res = a**b
        assert res == raise_to_power(a, b)

    def test_is_palindrome(self):
        s = 'madam'
        assert is_palindrome(s)
        s = '123'
        assert not is_palindrome(s)

    def test_compute_fibonnaci(self):
        n = 7
        assert 13 == compute_fibonnaci(n)
        n = 0
        assert 0 == compute_fibonnaci(n)
        n = 1
        assert 1 == compute_fibonnaci(n)
        n = 2
        assert 1 == compute_fibonnaci(n)


if __name__ == '__main__':
    unittest.main()
