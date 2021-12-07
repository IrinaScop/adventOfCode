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
def mostFrequentBit(mylist, index, commonValue):
#--------------------------------------------------
    zeros = 0
    ones = 0
    mfb = ''

    for row in range(len(mylist)-1):
        print("ROUND: ",row)
        if ((mylist[row])[index]) == "0":
            zeros = zeros + 1
        elif ((mylist[row])[index]) == "1":
            ones = ones + 1

        if zeros > ones:
            mfb = "0"
        elif zeros < ones:
            mfb = "1"
        
        elif zeros == ones and commonValue == "least":
                mfb = "0"
        elif zeros == ones and commonValue == "most":
                mfb = "1"
    return mfb

#-------------------------------------------------- 
def createMultiplier(myList):
#--------------------------------------------------
    lenOflist = len(myList[1])
    newList = []
    pattern = ''

    for i in range(lenOflist):
        #find most commont bit and add to pattern
        # append elements tha match pattern
        #do it for all elements in (every)newList until there is one element left

    return newList

#-------------------------------------------------- 
def multiplier(mylist):
#--------------------------------------------------
    oxygen = []
    oc2 = mylist
    lenOflist = len(mylist[1])

    oxygen = createMultiplier(mylist)

    #print(oxygen, oc2)

    return oxygen

#-------------------------------------------------- 
def binaryToDecimal(binaryNumber):
#--------------------------------------------------
    print(int(str(binaryNumber[0])))
    dec = (binaryNumber[0])
    dec = int(str(binaryNumber[0]),2)
    print(dec)

    return int(dec)

#-------------------------------------------------- 
def main():
#--------------------------------------------------
    binaryList=[]
    binaryList = createlist("binary_test.txt", "r")
    oxygen = multiplier(binaryList)

    dec_oxygen = binaryToDecimal(oxygen)
    #decimal_oc2 = binaryToDecimal(oc2)
    print(dec_oxygen)

    print("Binary number gamma:", oxygen, " is equal to decimal number:",dec_oxygen)
    #print("Binary number epsilon:", oc2, " is equal to epsilon number:",decimal_oc2)
    #print("The power consumption of the submarine is gamma multuplied by epsilon = ", (dec_gamma*decimal_epsilon))


if __name__ == "__main__":

    # calling main function
    main()
