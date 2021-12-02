# Python code to
# demonstrate readlines()
 
mylist = []
sum_list = []
 
# Using readlines()
file = open('numbers_list.txt', 'r')
Lines = file.readlines()
 
# Strips the newline character
for line in Lines:
    mylist.append(int(line.strip()))
    #print("Line{}: {}".format(count, line.strip()))

for i in range(0,len(mylist)-2):
    sum_list.append(mylist[i] +mylist[i+1] + mylist[i+2])

count = 0

for i in range(len(sum_list)-1):
    if sum_list[i] < sum_list[i+1]:
        count = count + 1


#print(mylist'\n')
print(count)