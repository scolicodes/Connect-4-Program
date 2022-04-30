# Name: Michael Scoli

class Board:
    def __init__(self, width=7, height=6):
        """Board object constructor that takes in two named arguments for number of rows and
        number of columns, and also initializes a game area represented by a 2-D list"""
        self.width = width
        self.height = height
        gameArea = []
        for column in range(self.width):
            gameArea.append([])
            for row in range(self.height):
                gameArea[column].append(' ')

        self.gameArea = gameArea

    def __str__(self):
        """Returns a string represent the Board object that calls it"""
        output = ''
        for rowIndex in range(self.height):
            for column in self.gameArea:
                output += '|' + column[rowIndex]

            output += '|\n'

        for i in range(self.width * 2 + 1):
            output += '-'
        output += '\n '

        colNums = list(range(self.width))
        colNums = list(map(lambda x: str(x), colNums))
        output += ' '.join(colNums)

        return output

    def allowsMove(self, col):
        """Returns True if the instance Board object can allow a move into column col
        (b/c there is space available)"""
        isEmptySpace = False

        for space in self.gameArea[col]:
            if space == ' ':
                isEmptySpace = True

        return isEmptySpace

    def addMove(self, col, ox):
        """Adds ox checker, where ox is a variable holding a string that is either 'X' or 'O',
        into the highest row number available in column col."""
        for i in range(self.height):
            if self.gameArea[col][i] == ' ':
                highestRowNumAvail = i
        self.gameArea[col][highestRowNumAvail] = ox

    def setBoard(self, moveString):
        """takes in a string of columns and places
        alternating checkers in those columns, starting with 'X'
        For example, call b.setBoard('0123456') to see 'X's and 'O's alternate on the bottom row, or b.setBoard('000000') to see them alternate in the left column.
        moveString must be a string of integers"""

        nextCh = 'X'  # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'

    def winsFor(self, ox):
        """Returns True if given checker, 'X' or 'O', held in ox, has won the calling
        Board"""
        # Check if player has won horizontally
        for i in range(self.height):
            oxCounter = 0
            for j in range(self.width):
                if self.gameArea[j][i] == ox:
                    oxCounter += 1
                    if oxCounter == 4:
                        return True
                else:
                    oxCounter = 0

        # Check if player has won vertically
        for i in range(self.width):
            oxCounter = 0
            for j in range(self.height):
                if self.gameArea[i][j] == ox:
                    oxCounter += 1
                    if oxCounter == 4:
                        return True
                else:
                    oxCounter = 0

        # Check if player has won diagonally (positive slope)
        for i in range(self.height - 3, self.height):
            oxCounter = 0
            currRow = i
            currCol = 0
            while currRow >= 0 and currCol <= self.width - 1:
                if self.gameArea[currCol][currRow] == ox:
                    oxCounter += 1
                    if oxCounter == 4:
                        return True
                else:
                    oxCounter = 0
                currCol += 1
                currRow -= 1

        for i in range(1, self.width - 3):
            oxCounter = 0
            currRow = self.height - 1
            currCol = i
            while currRow >= 0 and currCol <= self.width - 1:
                if self.gameArea[currCol][currRow] == ox:
                    oxCounter += 1
                    if oxCounter == 4:
                        return True
                else:
                    oxCounter = 0
                currCol += 1
                currRow -= 1

        # Check if player has won diagonally (negative slope)
        for i in range(self.height - 4, -1, -1):
            oxCounter = 0
            currRow = i
            currCol = 0
            while currRow <= self.height - 1 and currCol <= self.width - 1:
                if self.gameArea[currCol][currRow] == ox:
                    oxCounter += 1
                    if oxCounter == 4:
                        return True
                else:
                    oxCounter = 0
                currCol += 1
                currRow += 1

        for i in range(1, self.width - 4):
            oxCounter = 0
            currRow = 0
            currCol = i
            while currRow <= self.height - 1 and currCol <= self.width - 1:
                if self.gameArea[currCol][currRow] == ox:
                    oxCounter += 1
                    if oxCounter == 4:
                        return True
                else:
                    oxCounter = 0
                currCol += 1
                currRow += 1

    def hostGame(self):
        """Runs loop allowing the user(s) to play a game"""
        runGame = True
        currPlayer = "X"
        print("Welcome to Connect Four!")

        while runGame:
            print('\n' + self.__str__() + '\n')

            playerChoice = int(input(currPlayer + "'s choice: "))

            if playerChoice not in range(self.width):
                print("Error: Column #" + str(playerChoice) + " does not exist in this game board")
            elif not self.allowsMove(playerChoice):
                print("No spaces available in column # " + str(playerChoice))
            else:
                self.addMove(playerChoice, currPlayer)

                if self.winsFor(currPlayer):
                    print('\n' + currPlayer + " wins -- Congratulations!\n")
                    print(self)
                    runGame = False
                else:
                    if currPlayer == 'X':
                        currPlayer = 'O'
                    else:
                        currPlayer = 'X'

# b = Board()
# b.hostGame()



