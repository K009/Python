line = " Ala ma kota i psa "
firstWord = ""
secondWord = ""

list_line = line.split()

for character in list_line:
	firstWord += character[0]

for character in list_line:
	secondWord += character[len(character) -1]

print(firstWord)
print(secondWord)
