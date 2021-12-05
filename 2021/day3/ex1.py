#-----------------------------------
def createlist(txt, mode):
#-----------------------------------
    f=open(txt, mode)

    Lines=f.readlines()
    binaryList=[]

    for line in Lines:
        binaryList.append(line.rstrip())
    f.close()

    return binaryList

#-------------------------------------------------- 
def mostFrequentBit(mylist, i):
#--------------------------------------------------
    zeros = 0
    ones = 0

    for y in range(len(mylist)):
        if ((mylist[y])[i]) == "0":
            zeros = zeros + 1
        elif ((mylist[y])[i]) == "1":
            ones = ones + 1
    return zeros, ones

#-------------------------------------------------- 
def createBinaryNumbers(zeros,ones,g,e):
#--------------------------------------------------
    gamma = g
    epsilon = e

    if zeros > ones:
        gamma = gamma + "0"
        epsilon= epsilon + "1"
    elif ones > zeros:
        gamma = gamma + "1"
        epsilon= epsilon + "0"
    return gamma, epsilon

#-------------------------------------------------- 
def findBinaryNumbers(mylist):
#--------------------------------------------------
    binaryList = mylist

    lenOflist = len(binaryList[1])

    print(lenOflist)

    gamma = ''
    epsilon = ''

    for i in range(lenOflist):
        zeros, ones = mostFrequentBit(mylist, i) 
        gamma, epsilon = createBinaryNumbers(zeros,ones, gamma, epsilon)
    return gamma, epsilon

#-------------------------------------------------- 
def main():
#--------------------------------------------------
    binaryList=[]
    binaryList = createlist("binary.txt", "r")
    gamma, epsilon = findBinaryNumbers(binaryList)

    dec_gamma = int(gamma, 2)
    decimal_epsilon = int(epsilon, 2)

    print("Binary number gamma:", gamma, " is equal to decimal number:",dec_gamma)
    print("Binary number epsilon:", epsilon, " is equal to epsilon number:",decimal_epsilon)

    print("The power consumption of the submarine is gamma multuplied by epsilon = ", (dec_gamma*decimal_epsilon))


if __name__ == "__main__":

    # calling main function
    main()
