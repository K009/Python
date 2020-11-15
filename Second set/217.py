line = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."


line_split = line.split()

print(sorted(line_split, key=str.lower))
print(sorted(line_split, key=len))