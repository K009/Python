def moda_py(L, left, right):
	if not (isinstance(left,int) or isinstance(right, int)) or right <0 or left <0:
		raise ValueError("Left i right nie moga byc mniejsze od zera")
	if right < left:
		raise ValueError("Right nie moze byc mniejszy od left")
    
    howMany = dict()

    for i in range (left, right):
        howMany[L[i]] = howMany.get(L[i],0) +1
    return max(howMany, key=howMany.get)

newList = 