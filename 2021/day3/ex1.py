f=open("binary.txt","r")

Lines=f.readlines()
binary_list=[]

for line in Lines:
    binary_list.append(line.rstrip())
f.close()

len_of_nummber = len(binary_list[1])

gamma = ''
epsilon = ''

for i in range(len_of_nummber):
    zeros = 0
    ones = 0
    for y in range(len(binary_list)):

        if ((binary_list[y])[i]) == "0":
            zeros = zeros + 1
        elif ((binary_list[y])[i]) == "1":
            ones = ones + 1

    if zeros > ones:
        gamma = gamma + "0"
        epsilon= epsilon + "1"
    elif ones > zeros:
        gamma = gamma + "1"
        epsilon= epsilon + "0"

dec_gamma = int(gamma, 2)
decimal_epsilon = int(epsilon, 2)

print("Binary number gamma:", gamma, " is equal to decimal number:",dec_gamma)
print("Binary number epsilon:", epsilon, " is equal to epsilon number:",decimal_epsilon)

print("The power consumption of the submarine is gamma multuplied by epsilon = ", (dec_gamma*decimal_epsilon))

