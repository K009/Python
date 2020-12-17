class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):             # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):             # nigdy nie jest pusta
        return False

    def put(self, data):
        if self.is_full():
            raise ValueError("kolejka jest pelna")
        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise ValueError("pusta kolejka")
        return self.items.pop(0)   # mało wydajne!

kolejka = Queue()
kolejka.put(28)
kolejka.put(38)
print(kolejka.is_empty())
print(kolejka.__str__())

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.k1 = Queue()
        self.k2 = Queue()
        self.k3 = Queue()
        self.k1.put(1)
        self.k1.put(2)
        self.k3.put(101)

    def test_str_put(self):
        self.assertEqual(str(self.k1), "[1, 2]")
        self.assertEqual(str(self.k3), "[101]")        

    def test_is_empty(self):
        self.assertFalse(self.k1.is_empty())
        self.assertTrue(self.k2.is_empty())        

    def test_is_full(self):
        self.assertFalse(self.k1.is_full())
        self.assertFalse(self.k2.is_full())
        self.assertFalse(self.k3.is_full())

    def test_get(self):
        self.assertEqual(self.k1.get(), 1)
        self.assertEqual(self.k3.get(), 101)

if __name__ == "__main__":
        unittest.main()