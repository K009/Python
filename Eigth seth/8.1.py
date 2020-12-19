def solve1(a, b, c):
	"""Rozwiązywanie równania liniowego a x + b y + c = 0."""
	i = 0
	while i * a <= c: 
		if (-c - (i * a)) % b == 0: 
			print("x = ",i ,", y = ", 
			((-c - (i * a)) / b)) 
			return 0
		i = i + 1
	
	print("Brak rozwiazania")     

a = 2
b = 3
c = 7
solve1(a, b, c) 
