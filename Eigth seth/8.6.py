def solve(i, j):

	P = {}

	if i<0 or j <0:
		raise TypeError('Numbers cannot be negative')
	P[(0, 0)] = 0.5
	for x in range (1, i+1):
		P[(x, 0)] = 0.0

	for y in range (1, j+1):
		P[(0, y)] = 1.0

	for z in range (1, i+1):
		for o in range (1, j+1):
			P[(z, o)] = 0.5 * P[(z-1, o)] + P[(z, o-1)]

	return P.get((i, j))	

i = 0
j = 0
print(solve(i, j) )


