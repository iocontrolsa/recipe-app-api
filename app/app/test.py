"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """ test for adding 2 numbers """

    def test_add_numbers(self):
        """ Adding Numbers Together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Subtracting number """
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
