def mediana_sort(L, left, right):
	if not (isinstance(left,int) or isinstance(right, int)) or right <0 or left <0:
		raise ValueError("Left i right nie moga byc mniejsze od zera")
	if right < left:
		raise ValueError("Right nie moze byc mniejszy od left")

	list = sorted(L[left:right])
	if len(list) %2 == 0:
		tmp = (len(list)-1)//2
		return (list[tmp]+list[tmp+1])/2

	return list[(len(list))//2]

L=[22,43,11,-3,54,23]

print(mediana_sort(L,0,len(L)))