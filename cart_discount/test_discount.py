import unittest 
from unittest import TestCase

from cart_discount import price_discount
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    # more unit tests here. Each test should test one scenario
    def test_list_of_two_prices(self):
        prices = [1, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_one_price(self):
        prices = [4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_empy_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))


    # invalid data scenarios

    # 0 is falsy value!
    def test_zero_in_price_list(self):
        prices = [0, 4, 10]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    # none is falsy value!
    def test_None_for_price(self):
        prices = None
        self.fail('finish me')

    def test_string_in_price_list(self):
        prices = ['a', 'b', 'c']
        self.fail('finish me')

    def test_string_instead_of_list(self):
        prices = 'Cat'
        self.fail('finish me')

    def test_negative_numbers_in_price_list(self):
        prices = [-5, -2, 7]
        self.fail('finish me')

    def test_floating_points_in_price_list(self):
        prices = [6.99, 4.5, 3.72]
        self.fail('finish me')

    # string of numbers ('1', '2', '3', ...)



if __name__ == '__main__':
    unittest.main()