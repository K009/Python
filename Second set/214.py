line = "Ala ma kota i psa"
maximum = 0
maximumWord = ""
list_line = line.split()

for character in list_line:
	if maximum < len(character):
		maximum = len(character)
		maximumWord = character

print(maximumWord)
print(len(maximumWord))
