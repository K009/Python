import fractions

def is_fraction_correct(frac):
	if frac[1] == 0:
		return False
	if not isinstance(frac[0], int) or not isinstance(frac[1], int):
		return False
	return True

def add_frac(frac1, frac2):
    if not is_fraction_correct(frac1) or not is_fraction_correct(frac2):
        raise TypeError("Denominator can't be zero, also all number must be integers.")
    leastMultiplier = frac1[1]*frac2[1] // fractions.gcd(frac1[1], frac2[1])

    frac1[0] = frac1[0] * leastMultiplier // frac1[1]
    frac2[0] = frac2[0] * leastMultiplier // frac2[1]
    
    frac1[1] = leastMultiplier
    frac2[1] = leastMultiplier

    return [frac1[0] + frac2[0],frac1[1]]

def sub_frac(frac1, frac2):
    if not is_fraction_correct(frac1) or not is_fraction_correct(frac2):
        raise TypeError("Denominator can't be zero, also all number must be integers.")
    leastMultiplier = frac1[1]*frac2[1] // fractions.gcd(frac1[1], frac2[1])

    frac1[0] = frac1[0] * leastMultiplier // frac1[1]
    frac2[0] = frac2[0] * leastMultiplier // frac2[1]
    
    frac1[1] = leastMultiplier
    frac2[1] = leastMultiplier

    return [frac1[0] - frac2[0],frac1[1]]

def mul_frac(frac1, frac2):
    if not is_fraction_correct(frac1) or not is_fraction_correct(frac2):
        raise TypeError("Denominator can't be zero, also all number must be integers.")

    frac1[0] = frac1[0]*frac2[0]
    frac1[1] = frac1[1]*frac2[1]

    return frac1

def div_frac(frac1, frac2):
    if not is_fraction_correct(frac1) or not is_fraction_correct(frac2):
        raise TypeError("Denominator can't be zero, also all number must be integers.")

    frac2[0], frac2[1] = frac2[1], frac2[0]

    return mul_frac(frac1, frac2)

def is_positive(frac):
    if not is_fraction_correct(frac):
        raise TypeError("Denominator can't be zero, also all number must be integers.")

    if frac[0] < 0 and frac[1] < 0:
        frac[0] = abs(frac[0])
        frac[1] = abs(frac[1])    

    if frac[0] < 0 and frac[1] < 0 or frac[0] > 0 and frac[1] > 0:
    	return True
    return False    

def is_zero(frac):
    if not is_fraction_correct(frac):
        raise TypeError("Denominator can't be zero, also all number must be integers.")
    if frac[0] == 0:
    	return True
    else:
    	return False

def cmp_frac(frac1, frac2):
    if not is_fraction_correct(frac1) or not is_fraction_correct(frac2):
        raise TypeError("Denominator can't be zero, also all number must be integers.")

    leastMultiplier = frac1[1]*frac2[1] // fractions.gcd(frac1[1], frac2[1])

    frac1[0] = frac1[0] * leastMultiplier // frac1[1]
    frac2[0] = frac2[0] * leastMultiplier // frac2[1]
    
    frac1[1] = leastMultiplier
    frac2[1] = leastMultiplier

    if frac1[0] > frac2[0]:
    	return 1
    if frac1[0] < frac2[0]:
    	return -1
    else:
    	return 0        

def frac2float(frac):
    if not is_fraction_correct(frac):
        raise TypeError("Denominator can't be zero, also all number must be integers.")
    return float(frac[0]) / float(frac[1])    	

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        with self.assertRaises(TypeError):
        	add_frac([6, 0], [1, 2])

    def test_sub_frac(self):
    	self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
    	with self.assertRaises(TypeError):
            sub_frac([6, 0], [1, 2])

    def test_mul_frac(self):
    	self.assertEqual(mul_frac([2, 3], [1, 3]), [2, 9])
    	with self.assertRaises(TypeError):
            mul_frac([6, 0], [1, 2])

    def test_div_frac(self):
    	self.assertEqual(div_frac([2, 3], [1, 3]), [6, 3])
    	with self.assertRaises(TypeError):
            div_frac([6, 0], [1, 2])

    def test_is_positive(self):
        self.assertTrue(is_positive([9, 5]))
        self.assertFalse(is_positive([-9, 5]))        
        with self.assertRaises(TypeError):
            is_positive([7.8, 4.4])

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 3]))
        self.assertFalse(is_zero([9, 5]))
        with self.assertRaises(TypeError):
            is_zero([0, 0])

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 5], [2, 3]), -1)
        self.assertEqual(cmp_frac([1, -2], [1, 2]), 1)
        with self.assertRaises(TypeError):
            cmp_frac([3, 0], [1.2, 3])

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 5]), 0.2)
        self.assertEqual(round(frac2float([11, 33]), 2), 0.33)  	

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy