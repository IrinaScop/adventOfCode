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

        if zeros > ones:
            mfb = "0"
        elif zeros < ones:
            mfb = "1"
    return mfb

#-------------------------------------------------- 
def createMultipliers(mfb,g,e):
#--------------------------------------------------
    mostFreqBit = mfb
    gamma = g
    epsilon = e

    if (mostFreqBit == "1"):
        gamma = gamma + "0"
        epsilon= epsilon + "1"
    elif (mostFreqBit == "0"):
        gamma = gamma + "1"
        epsilon= epsilon + "0"
    return gamma, epsilon

#-------------------------------------------------- 
def multipliers(mylist):
#--------------------------------------------------
    binaryList = mylist

    lenOflist = len(binaryList[1])

    print(lenOflist)

    gamma = ''
    epsilon = ''

    for i in range(lenOflist):
        mfb = mostFrequentBit(mylist, i) 
        gamma, epsilon = createMultipliers(mfb, gamma, epsilon)
    return gamma, epsilon

#-------------------------------------------------- 
def main():
#--------------------------------------------------
    binaryList=[]
    binaryList = createlist("binary.txt", "r")
    gamma, epsilon = multipliers(binaryList)

    dec_gamma = int(gamma, 2)
    decimal_epsilon = int(epsilon, 2)

    print("Binary number gamma:", gamma, " is equal to decimal number:",dec_gamma)
    print("Binary number epsilon:", epsilon, " is equal to epsilon number:",decimal_epsilon)

    print("The power consumption of the submarine is gamma multuplied by epsilon = ", (dec_gamma*decimal_epsilon))


if __name__ == "__main__":

    # calling main function
    main()
