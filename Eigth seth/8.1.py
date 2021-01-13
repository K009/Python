def solve1(a, b, c):
	"""Rozwiązywanie równania liniowego a x + b y + c = 0."""
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
		raise TypeError("Parametry muszą być liczbami")
	if a == 0 and b == 0:
		if c != 0:
			print("Równanie jest sprzeczne")
			return
		else:
			print("Równanie nieoznaczone, czyli opisuje cala powierzchnie")
			return
	if b != 0:
		a1 = -(a/b)
		c1 = -(c/b)
		print(f"Równanie opisuje prostą postaci: y = ({a1})x + ({c1})")
		return
	elif b == 0:
		c1 = -(c/a)
		print(f"Równanie opisuje prostą postaci: x = {c1}")
		return    


solve1(a=2,b=3,c=7) #prosta y=-0.66x - 2.33
solve1(a=0,b=0,c=0) #nieoznaczone
solve1(a=1,b=0,c=0) #prosta x=0
solve1(a=0,b=0,c=1) #sprzeczne
