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
def mostFrequentBit(mylist, x):
#--------------------------------------------------
    zeros = 0
    ones = 0

    for row in range(len(mylist)):
        if ((mylist[row])[x]) == "0":
            zeros = zeros + 1
        elif ((mylist[row])[x]) == "1":
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
        mfb = mostFrequentBit(binaryList, i) 
        gamma, epsilon = createMultipliers(mfb, gamma, epsilon)
    return gamma, epsilon

#-------------------------------------------------- 
def binaryToDecimal(binaryNumber):
#--------------------------------------------------
    dec = binaryNumber
    dec= int(binaryNumber, 2)

    return dec

#-------------------------------------------------- 
def main():
#--------------------------------------------------
    binaryList=[]
    binaryList = createlist("binary.txt", "r")
    gamma, epsilon = multipliers(binaryList)

    dec_gamma = binaryToDecimal(gamma)
    decimal_epsilon = binaryToDecimal(epsilon)

    print("Binary number gamma:", gamma, " is equal to decimal number:",dec_gamma)
    print("Binary number epsilon:", epsilon, " is equal to epsilon number:",decimal_epsilon)
    print("The power consumption of the submarine is gamma multuplied by epsilon = ", (dec_gamma*decimal_epsilon))


if __name__ == "__main__":

    # calling main function
    main()
