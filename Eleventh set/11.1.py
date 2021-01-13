from numpy import random

def swapPositions(list):
	j = 0
	for i in list:
		if(j+1 == len(list)):
			return list
		if(i!= list[j+1]):
			list[j], list[j+1] = list[j+1], list[j]
			return list
		j = j+1
	return list

def optionA(size):
	list = [0,1,2,3,4,5,6,7,8,9]
	random.shuffle(list)
	return list

def optionB(size):
	list = []
	while len(list) < size-1:
		element = random.randint(0,size-1)
		if element not in list:
			list.append(element)
	list.sort()
	swapPositions(list)
	return list

def optionC(size):
	list = []
	while len(list) < size-1:
		element = random.randint(0,size-1)
		if element not in list:
			list.append(element)
	list.sort(reverse=True)
	swapPositions(list)
	return list	

def optionD(size):
	list = []
	for i in range(0,size):
		list.append(float(random.normal(size=1)))
	return list	

def optionE(n, k):
	list = []
	if n <=k:
		raise ValueError("k nie moze byc wieksze ani rowne n")
	for i in range(n):
		list.append(random.randint(0,k-1))	
	return list		

print(optionE(20,18))