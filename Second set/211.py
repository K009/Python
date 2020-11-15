line = "word"
readyLine =""

for character in line:
	if not character == line[-1]:
		readyLine += character + "_"
	else:
		readyLine+= character

print(readyLine)