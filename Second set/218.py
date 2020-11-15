line = 645364034324
placeWherZeroIs = 0 

for element in str(line):
	if(int(element) == 0):
		break
	placeWherZeroIs += 1

print(placeWherZeroIs)