def intersection(sequence1, sequence2):
	print('INTERSECTION:')
	if(isinstance(sequence1, tuple)):
		sequence1 = sorted(sequence1)
	else:
		sequence1.sort()
	if(isinstance(sequence2, tuple)):
		sequence2 = sorted(sequence2)
	else:
		sequence2.sort()

	result = []

	for elem1 in sequence1:
		for elem2 in sequence2:
			if elem1 < elem2:
				break
			elif elem1 == elem2:
				if elem1 not in result:
					result.append(elem1)
	return result

def sum(sequence1, sequence2):
	print('SUM:')
	sequence1 = list(dict.fromkeys(sequence1))
	result = []

	for elem1 in sequence1:
		if elem1 not in result:
			result.append(elem1)
	return result


firstList = ['a', 'b', 'c', 'gf', 'bdd']
secondList = ['bdd', 'x', 'y', 'z','a','a']

print(intersection(firstList, secondList))
print(sum(firstList, secondList))