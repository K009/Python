line = "Ala ma kota i psa"
suma = 0
list_line = line.split()

for character in list_line:
	#print(character)
	suma += len(character)
print(suma)