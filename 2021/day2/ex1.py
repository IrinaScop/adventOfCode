x = 0
y = 0

file= open("course.txt")


for line in file:
    whereto, value = line.split()

    if whereto ==  'down': 
        x = x + int(value)

    if whereto ==  'up': 
        x = x - int(value)

    if whereto == 'forward': 
        y = y + int(value)

print(x," * ", y," = ",(x*y))