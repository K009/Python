line = "Lorem Ipsum is simply dummy text of the printing and typesetting industry, but GvRx should be changed to something else, right GvR ?"

line_split = line.split()
line = ""

for element in line_split:
	if('GvR' in element):
		element = 'Gudio van Rossum'
	line += element + ' '

print(line)
