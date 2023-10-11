import random

print("Welcome to Connect Four Game")
print("----------------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "]]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🟡":
                print(" 🟡 |", end="")
            elif gameBoard[x][y] == "🔴":
                print(" 🔴 |", end="")
            else:
                print("    |", end="")
        print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    for y in range(rows):
        for x in range(cols - 3):
            if (
                gameBoard[x][y] == chip
                and gameBoard[x + 1][y] == chip
                and gameBoard[x + 2][y] == chip
                and gameBoard[x + 3][y] == chip
            ):
                return True

    for x in range(rows):
        for y in range(cols - 3):
            if (
                gameBoard[x][y] == chip
                and gameBoard[x][y + 1] == chip
                and gameBoard[x][y + 2] == chip
                and gameBoard[x][y + 3] == chip
            ):
                return True

    for x in range(rows - 3):
        for y in range(3, cols):
            if (
                gameBoard[x][y] == chip
                and gameBoard[x + 1][y - 1] == chip
                and gameBoard[x + 2][y - 2] == chip
                and gameBoard[x + 3][y - 3] == chip
            ):
                return True

    for x in range(rows - 3):
        for y in range(cols - 3):
            if (
                gameBoard[x][y] == chip
                and gameBoard[x + 1][y + 1] == chip
                and gameBoard[x + 2][y + 2] == chip
                and gameBoard[x + 3][y + 3] == chip
            ):
                return True
    return False

def coordinateParser(inputString):
    coordinate = [None] * 2
    if inputString[0] == "A":
        coordinate[1] = 0
    elif inputString[0] == "B":
        coordinate[1] = 1
    elif inputString[0] == "C":
        coordinate[1] = 2
    elif inputString[0] == "D":
        coordinate[1] = 3
    elif inputString[0] == "E":
        coordinate[1] = 4
    elif inputString[0] == "F":
        coordinate[1] = 5
    elif inputString[0] == "G":
        coordinate[1] = 6
    else:
        print("Invalid")
    coordinate[0] = int(inputString[1])
    return coordinate

def isSpaceAvailable(intendedCoordinate):
    column = intendedCoordinate[1]
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][column] != '🔴' and gameBoard[row][column] != '🟡':
            return True
    return False

def gravityChecker(intendedCoordinate):
    column = intendedCoordinate[1]
    if gameBoard[0][column] == '🔴' or gameBoard[0][column] == '🟡':
        return False
    return True

leaveLoop = False
turnCounter = 0
while not leaveLoop:
    if turnCounter % 2 == 0:
        printGameBoard()
        while True:
            spacePicked = input("\nPlayer 1 (🟡), choose a space: ")
            coordinate = coordinateParser(spacePicked)
            if coordinate is not None and isSpaceAvailable(coordinate) and gravityChecker(coordinate):
                modifyArray(coordinate, '🟡')
                if checkForWinner('🟡'):
                    printGameBoard()
                    print("Player 1 (🟡) wins! Thank you for playing :)")
                    leaveLoop = True
                break
            elif coordinate is not None:
                print("Invalid move. Please choose a valid column that is not full.")
    else:
        while True:
            spacePicked = input("\nPlayer 2 (🔴), choose a space: ")
            coordinate = coordinateParser(spacePicked)
            if coordinate is not None and isSpaceAvailable(coordinate) and gravityChecker(coordinate):
                modifyArray(coordinate, '🔴')
                if checkForWinner('🔴'):
                    printGameBoard()
                    print("Player 2 (🔴) wins! Thank you for playing :)")
                    leaveLoop = True
                break
    turnCounter += 1

    # Check for a draw
    if turnCounter == rows * cols:
        printGameBoard()
        print("It's a draw! Thank you for playing :)")
        leaveLoop = True