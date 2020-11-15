def factorial(n):
	result = 1
	i = 1
	while i < n:
		i = i + 1
		result = result * i
	return result


def fibonacci(n):
	a = 0
	b = 1
	i = 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		while i < n:
			i = i + 1
			b += a
			a = b-a
		return b