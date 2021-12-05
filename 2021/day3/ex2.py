#-----------------------------------
def createlist(txt, mode):
#-----------------------------------
    f=open(txt, mode)

    Lines=f.readlines()
    binary_list=[]

    for line in Lines:
        binary_list.append(line.rstrip())
    f.close()

    return binary_list

#-------------------------------------------------- 
def mostFrequent(mylist):
#--------------------------------------------------
    binary_list = mylist

    len_of_nummber = len(binary_list[1])

    print(len_of_nummber)

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
            print(gamma)
        elif ones > zeros:
            gamma = gamma + "1"
            epsilon= epsilon + "0"

    return gamma, epsilon

#-------------------------------------------------- 
def main():
#--------------------------------------------------
    binary_list=[]

    binary_list = createlist("binary.txt", "r")

    gamma, epsilon = mostFrequent(binary_list)

    dec_gamma = int(gamma, 2)
    decimal_epsilon = int(epsilon, 2)

    print("Binary number gamma:", gamma, " is equal to decimal number:",dec_gamma)
    print("Binary number epsilon:", epsilon, " is equal to epsilon number:",decimal_epsilon)

    print("The power consumption of the submarine is gamma multuplied by epsilon = ", (dec_gamma*decimal_epsilon))


if __name__ == "__main__":

    # calling main function
    main()
