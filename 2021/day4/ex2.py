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
def lastWinningBoard(bingoNumbers,board, checkBoards):
#--------------------------------------------------
    allBoardsWon = False
    winboard = []
    winnumber = []

    wincheckboard = []

    bingo = 0

    bingoFound = False

    for number in bingoNumbers:
        for i in range(len(board)):
            for y in range(len(board[0][0])):
                bingo = 0
                rowFound = False
                for z in range(len(board[0])):
                    if(len(winboard) == len(board)):
                        wincheckboard = checkBoards
                        bingoFound = True
                        break
                    if (board[i][y][z] == number):
                        checkBoards[i][y][z] = '1'
                    if(checkBoards[i][y][z] == '1'):
                        bingo = bingo + 1
                    if(bingo == 5):
                        if(i not in winboard):
                            winboard.append(i)
                            winnumber.append(number)
                            wincheckboard = checkBoards

                if(bingoFound):
                    break

            for z in range(len(board[0][0])):
                bingo = 0
                rowFound = False
                for y in range(len(board[0])):
                    if(len(winboard) == len(board)):
                        wincheckboard = checkBoards
                        bingoFound = True
                        break
                    if (board[i][y][z] == number):
                        checkBoards[i][y][z] = '1'
                    if(checkBoards[i][y][z] == '1'):
                        bingo = bingo + 1
                    if(bingo == 5):
                        if(i not in winboard):
                            winboard.append(i)
                            winnumber.append(number)

                if(bingoFound):
                    break

    #print(winnumber, winboard)
    #print("\n......",wnumber,"\n......",winboard)
    return (winboard[-1], wincheckboard[winboard[-1]],winnumber[-1])

#-------------------------------------------------- 
def calculateWinningBoardPoints(winningBoard,winningCheckBoard, winningNumber):
#--------------------------------------------------
    sumOfBoard = 0

    print(winningBoard)
    print(winningCheckBoard)

    for i in range(len(winningCheckBoard)):
        for y in range(len(winningCheckBoard[0])):
            if (winningCheckBoard[i][y] == '0'):
                    sumOfBoard = sumOfBoard + int(winningBoard[i][y])
    print(sumOfBoard)


    return (sumOfBoard*int(winningNumber))

#-------------------------------------------------- 
def main():
#--------------------------------------------------
    myList=[]
    winnerPoints=[]
    myList = createlist("bingo.txt", "r")
    board, checkBoards = createBoards(myList)

    bingoNumbers = (myList[0]).split(',')

    winningBoard, winningCheckBoard, winningNumber = lastWinningBoard(bingoNumbers,board,checkBoards)


    #lasWinningBoard = board[boardNumber[-1]]
    #lastWinningCheckBoard = checkBoards[boardNumber[-1]]

    winnerPoints = calculateWinningBoardPoints(board[winningBoard],winningCheckBoard,winningNumber)

    #print("BOARD:       ",lasWinningBoard,"\nCHECKBOARD",lastWinningCheckBoard,"\nNUMBER:",winningNumber[-1])
    print("Total score: ",winnerPoints)
 

if __name__ == "__main__":

    # calling main function
    main()