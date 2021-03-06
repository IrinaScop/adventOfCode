#-----------------------------------
def createlist(txt, mode):
#-----------------------------------
    f=open(txt, mode)

    Lines=f.readlines()
    myList=[]

    for line in Lines:
        myList.append(line.rstrip())
        f.close()

    return myList


#-------------------------------------------------- 
def createBoards(inputlist):
#--------------------------------------------------
    boards = []
    checkBoards = []
    
    zeros = ['0 0 0 0 0']

    for i in range(len(inputlist)):
        if (inputlist[i] == ''):
            board = []
            zeroBoard = []
            for y in range(5):
                board.append((inputlist[i+(y+1)]).split())
                zeroBoard.append((zeros[0]).split())
            boards.append(board)
            checkBoards.append(zeroBoard)
    
    return boards, checkBoards

#--------------------------------------------------
def findWinningBoard(bingoNumbers,board, checkBoards):
#--------------------------------------------------
    bingoFound = False

    for number in bingoNumbers:
        for i in range(len(board)):
            for y in range(len(board[0][0])):
                bingo = 0
                rowFound = False
                for z in range(len(board[0])):
                    if (board[i][y][z] == number):
                        checkBoards[i][y][z] = '1'
                    if(checkBoards[i][y][z] == '1'):
                        bingo = bingo + 1
                    if(bingo == 5):
                        bingoFound = True
                        break

            for z in range(len(board[0][0])):
                bingo = 0
                rowFound = False
                for y in range(len(board[0])):
                    #print(board[i][y][z])
                    if (board[i][y][z] == number):
                        checkBoards[i][y][z] = '1'
                    if(checkBoards[i][y][z] == '1'):
                        bingo = bingo + 1
                    if(bingo == 5):
                        bingoFound = True
                        break
                if(bingoFound):
                    break
            if(bingoFound):
                break
        if(bingoFound):
            break


    #print(checkBoards)
    return (board[i], checkBoards[i], number)

#-------------------------------------------------- 
def calculateWinningBoardPoints(winningBoard,winningCheckBoard, winningNumber):
#--------------------------------------------------
    sumOfBoard = 0

    for i in range(len(winningBoard)):
        for y in range(len(winningBoard[0])):
            if (winningCheckBoard[i][y]== '0'):
                    sumOfBoard = sumOfBoard + int(winningBoard[i][y])


    return (sumOfBoard*int(winningNumber))

#-------------------------------------------------- 
def main():
#--------------------------------------------------
    myList=[]
    myList = createlist("bingo.txt", "r")
    board, checkBoards = createBoards(myList)

    bingoNumbers = (myList[0]).split(',')

    #print(len(board[0][0]))
    winningBoard, winningCheckBoard, winningNumber = findWinningBoard(bingoNumbers,board,checkBoards)
    winnerPoints = calculateWinningBoardPoints(winningBoard,winningCheckBoard,winningNumber)

    print("Total score: ",winnerPoints)
 

if __name__ == "__main__":

    # calling main function
    main()