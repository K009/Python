while 1:
	val1 = input("Enter any value: ")
	if val1 == 'stop':
		break;
	try:
		val1 = float(val1)
		print(val1)
		print(val1*val1*val1)
	except:
		print("WARNING! You entered string! It should be float number!")
