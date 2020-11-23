import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):       # Punkty jako wektory 2D v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny
        return Point(self.x * other.x,  self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return Point(self.x * other.y, - self.y * other.x)

    def length(self):          # długość wektora
        return round(math.sqrt(self.x**2 + self.y**2), 2)

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(-2, 3)
        self.p3 = Point(9, -3)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(self.p1.__eq__(Point(1, 2)))
        self.assertFalse(self.p1.__eq__(Point(2, 1)))

    def test_ne(self):
        self.assertTrue(self.p1.__ne__(Point(2, 2)))
        self.assertFalse(self.p2.__ne__(Point(-2, 3))) 

    def test_add(self):
        self.assertEqual(self.p1.__add__(self.p2), Point(-1, 5))
        self.assertEqual(self.p2.__add__(self.p3), Point(7, 0))

    def test_sub(self):
        self.assertEqual(self.p1.__sub__(self.p2), Point(3, -1))
        self.assertEqual(self.p2.__sub__(self.p3), Point(-11, 6))

    def test_mul(self):
        self.assertEqual(self.p1.__mul__(self.p2), Point(-2, 6))
        self.assertEqual(self.p2.__mul__(self.p3), Point(-18, -9))

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), Point(3, 4))
        self.assertEqual(self.p2.cross(self.p3), Point(6, -27))

    def test_length(self):
        self.assertEqual(self.p1.length(), 2.24)
        self.assertEqual(self.p2.length(), 3.61)
if __name__ == "__main__":
        unittest.main()