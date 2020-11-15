def factorial(n):
	result = 1
	i = 1
	while i < n:
		i = i + 1
		result = result * i
	return result

value = int(input('Enter a number:\n'))
print(factorial(value))