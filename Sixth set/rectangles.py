from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"        

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt2.x - self.pt1.x == other.pt2.x - other.pt1.x and self.pt2.y - self.pt1.y == other.pt2.y - other.pt1.y

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self.__eq__(other)

    def center(self):          # zwraca środek prostokąta
        return Point((self.pt2.x - (self.pt2.x - self.pt1.x) / 2), self.pt2.y - ((self.pt2.y - self.pt1.y) / 2))     

    def area(self):            # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)    

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle(1, 2, 3, 4)
        self.rectangle2 = Rectangle(4, 4, 6, 7)
        self.rectangle3 = Rectangle(1, 2, 3, 4)

    def test_str(self):
        self.assertEqual(self.rectangle1.__str__(), "[(1, 2), (3, 4)]")
        self.assertEqual(self.rectangle2.__str__(), "[(4, 4), (6, 7)]")

    def test_repr(self):
        self.assertEqual(self.rectangle1.__repr__(), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(self.rectangle2.__repr__(), "Rectangle(4, 4, 6, 7)")

    def test_eq(self):
        self.assertTrue(self.rectangle1.__eq__(self.rectangle1))
        self.assertFalse(self.rectangle2.__eq__(self.rectangle1))

    def test_ne(self):
        self.assertFalse(self.rectangle1.__ne__(self.rectangle1))
        self.assertTrue(self.rectangle2.__ne__(self.rectangle1))

    def test_center(self):
        self.assertEqual(self.rectangle1.center(), Point(2.0, 3.0))
        self.assertEqual(self.rectangle2.center(), Point(5.0, 5.5))

    def test_area(self):
        self.assertEqual(self.rectangle1.area(), 4)
        self.assertEqual(self.rectangle2.area(), 6)  

    def test_move(self):
        self.assertEqual(self.rectangle1.move(1, 1), Rectangle(2, 3, 4, 5))
        self.assertEqual(self.rectangle2.move(-2, -2), Rectangle(2, 2, 4, 5))     

if __name__ == "__main__":
    unittest.main()