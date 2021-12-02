# Python code to
# demonstrate readlines()
 
mylist = []
 
# Using readlines()
file = open('numbers_list.txt', 'r')
Lines = file.readlines()
 
# Strips the newline character
for line in Lines:

    mylist.append(int(line.strip()))
    #print("Line{}: {}".format(count, line.strip()))

count = 0

for i in range(len(mylist)-1):
    if mylist[i] < mylist[i+1]:
        count = count + 1


#print(mylist'\n')
print(count)