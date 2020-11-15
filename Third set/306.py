height = int(input("Enter rectangle's height:?\n"))
width = int(input("Enter rectangle's width:?\n"))
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
		print(wholeRectangle)
except:
	print(str(height) + ' and ' + str(width) + ' are not valid height and width, try again!!')
