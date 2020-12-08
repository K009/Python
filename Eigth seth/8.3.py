import random 
def calc_pi(n=100):
	"""Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
	punkty_kwadrat= 0
	punkty_kolo= 0

	for i in range(n): 
		los_x= random.uniform(-1, 1) 
		los_y= random.uniform(-1, 1) 

		dystans= los_x**2 + los_y**2

		if dystans<= 1: 
			punkty_kolo+= 1

		punkty_kwadrat+= 1
 
		pi = 4* punkty_kolo/ punkty_kwadrat

	return pi

print(calc_pi())
