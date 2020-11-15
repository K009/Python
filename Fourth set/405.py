def reverse(L, left, right):
	size = left + right
	for k in range(left, (size + 1) // 2):
		z = size - k
		L[k], L[z] = L[z], L[k]
	return L

L = [1,2,3,4,5,6,7,8,9,10]
left = 1
right = 8
print(reverse(L, left, right))