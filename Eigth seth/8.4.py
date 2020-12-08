import math
def heron(a, b, c):
	"""Obliczanie pola powierzchni trójkąta za pomocą wzoru
	Herona. Długości boków trójkąta wynoszą a, b, c."""
	if not isinstance(a, (float, int)) or not isinstance(b, (float, int)) or not isinstance(c, (float, int)):
		raise TypeError('BLAD! Podane parametry musza byc liczbami')
	if (((a+b>c) and (a+c>b)) and b+c>a):
		p = (a+b+c)/2
		S = math.sqrt(p*(p-a)*(p-b)*(p-c))
		return S   
	else:
		raise ValueError ('Zle dlugosci bokow!') 	

a = 3.0
b = 4.0
c = 5.0
print(heron(a,b,c))