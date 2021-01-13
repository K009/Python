def moda_py(L, left, right):
	if not (isinstance(left,int) or isinstance(right, int)) or right <0 or left <0:
		raise ValueError("Left i right nie moga byc mniejsze od zera")
	if right < left:
		raise ValueError("Right nie moze byc mniejszy od left")
    
    counter = dict()
    for element in range(left, right):
        counter[L[element]] = counter.get(L[element], 0) + 1
    return max(counter, key=counter.get)


L = [50, 8, 30, 54, 8, 50, 16, 65, 54, 50]
print(moda_py(L, 0, len(L)))        # returns 50