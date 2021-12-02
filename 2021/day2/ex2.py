x   = 0
y   = 0
aim = 0

file= open("course.txt")


for line in file:
    whereto, value = line.split()

    if whereto ==  'down':
        aim = aim + int(value) 

    if whereto ==  'up': 
        aim = aim - int(value) 

    if whereto == 'forward': 
        y = y + int(value)
        x = x + aim * int(value)

print(x," * ", y," = ",(x*y))