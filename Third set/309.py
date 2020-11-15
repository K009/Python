sequence = [[], [4], (1,2), [3,4], (5,6,7)]
result = []

for x in sequence:
	x = sum(list(x)) 
	result.append(x)
print(result)