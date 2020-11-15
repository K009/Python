val1 = int(input("How long should be the line?\n"))
try:
	if val1 < 0:
		exit()
	if val1 == 0:
		print('')
	else:
		for i in range(val1):
			print('|....', sep=' ', end='')
		print('|')
		for i in range(val1):
			lengthOfNumber = len(str(i))
			if lengthOfNumber == 1:
				print(str(i) +'    ', sep=' ', end='')	
			if lengthOfNumber == 2:
				print(str(i) +'   ', sep=' ', end='')
			if lengthOfNumber == 3:
				print(str(i) +'  ', sep=' ', end='')
			if lengthOfNumber == 4:
				print(str(i) +' ', sep=' ', end='')				
except:
	print(str(val1) + ' is not a valid length, try again!!')