def sum_seq(sequence):
	sum = 0
	for x in sequence:
		if(type(x) == type([])) or (isinstance(x, (list, tuple))):
			sum = sum + sum_seq(x)
		else:
			sum = sum + x
	return sum

sequence = [[1,2],[3,4,[2,2,[[5]]]],(5,(2,3),6)]
print(sum_seq(sequence))