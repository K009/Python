def mediana_sort(L, left, right):
	if not (isinstance(left,int) or isinstance(right, int)) or right <0 or left <0:
		raise ValueError("Left i right nie moga byc mniejsze od zera")
	if right < left:
		raise ValueError("Right nie moze byc mniejszy od left")

	sortedL = sorted(L[left:right])
	if len(sortedL) % 2 == 0:
    	    tmp = (len(sortedL)-1)//2
			return (sortedL[tmp]+sortedL[tmp+1])/2

L = [5, 4, 8, 7, 3]
print(mediana_sort(L, 0, len(L)))       # returns 5
L.append(2)
print(mediana_sort(L, 0, len(L)))       # returns 4.5

#   	return sortedL[(len(sortedL))//2]