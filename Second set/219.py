list = [3,4,12,16,145,276,189]
resultWord = ""

for element in list:
	element = str(element).zfill(3)
	resultWord += element + " "
print(resultWord)