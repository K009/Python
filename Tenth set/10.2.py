class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("stos jest pelny")        
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("stos jest pusty")        
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję


stos = Stack(size = 2)
stos.push(2)
stos.push(3)
stos.pop()
print(stos.__str__())


import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.s1 = Stack(size = 3)
        self.s2 = Stack()
        self.s3 = Stack(size = 1)
        self.s4 = Stack(size = 2)   
        self.s5 = Stack(size = 2)       
        self.s1.push(1)
        self.s1.push(2)
        self.s3.push(101)
        self.s4.push(320)
        self.s4.push(450)
        self.s5.push(11)        
        self.s4.pop()
        self.s5.pop()

    def test_str_push(self):
        self.assertEqual(str(self.s1), "[1, 2, None]")
        self.assertEqual(str(self.s3), "[101]")        

    def test_is_empty(self):
        self.assertFalse(self.s1.is_empty())
        self.assertTrue(self.s2.is_empty())        

    def test_is_full(self):
        self.assertFalse(self.s1.is_full())
        self.assertFalse(self.s2.is_full())
        self.assertTrue(self.s3.is_full())

    def test_str_pop(self):
        self.assertEqual(str(self.s4), "[320, None]")
        self.assertEqual(str(self.s5), "[None, None]") 

if __name__ == "__main__":
        unittest.main()        