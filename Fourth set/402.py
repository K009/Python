#3.05
def draw_a_line(val1):
	try:
		if val1 < 0:
			exit()
		if val1 == 0:
			return ''
		else:
			result = ''
			for i in range(val1):
				result += '|....'
			result +='|\n'
			for i in range(val1):
				result += str(i) + '    '
			return result
	except:
		print(str(val1) + ' is not a valid length, try again!!')

#3.06
def draw_a_rectangle(height, width):
	try:
		if (height < 1) or (width < 1):
			exit()
		else:
			rectangle_space = '|'
			rectangle_line = '+'
			wholeRectangle = ''
			for i in range(width):
				rectangle_space += '   |'
				rectangle_line += '---+'
			for i in range(height):
					wholeRectangle += rectangle_line + '\n' + rectangle_space + '\n'
			wholeRectangle += rectangle_line
			return wholeRectangle
	except:
		print(str(height) + ' and ' + str(width) + ' are not valid height and width, try again!!')

height = int(input("Enter rectangle's height:\n"))
width = int(input("Enter rectangle's width:\n"))
print(draw_a_rectangle(height, width))

val1 = int(input("How long should be the line?\n"))
print(draw_a_line(val1))