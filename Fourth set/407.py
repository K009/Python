def flatten(sequence, result):
	for x in sequence:
		if(type(x) == type([])) or (isinstance(x, (list, tuple))):
			flatten(x, result)
		else:
			result.append(x)
	return result

result = []
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq, result))            # [1,2,3,4,5,6,7,8,9]