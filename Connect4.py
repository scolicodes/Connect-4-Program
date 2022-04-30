# Name: Michael Scoli
import sys
import pygame
from math import floor

class Board:
    def __init__(self):
        """Board object constructor that takes in two named arguments for number of rows and
        number of columns, and also initializes a game area represented by a 2-D list"""
        self.width = 7
        self.height = 6
        gameArea = []
        self.BLUE = (0, 0, 225)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
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

    def drawBoard(self):
        for col in range(self.width):
            for row in range(self.height):
                pygame.draw.rect(screen, self.BLUE,(col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if self.gameArea[col][row] == ' ':
                    pygame.draw.circle(screen, self.BLACK, (int(col * SQUARE_SIZE + SQUARE_SIZE/2), int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE/2)), RADIUS)
                elif self.gameArea[col][row] == 'X':
                    pygame.draw.circle(screen, self.RED, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, self.YELLOW, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

                pygame.display.update()

    def hostGame(self):
        """Runs loop allowing the user(s) to play a game"""
        runGame = True
        currPlayer = "X"
        print("Welcome to Connect Four!")

        while runGame:
            self.drawBoard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, self.BLACK, (0, 0, width, SQUARE_SIZE))
                    if currPlayer == 'X':
                        posX = event.pos[0]
                        pygame.draw.circle(screen, self.RED, (posX, int(SQUARE_SIZE/2)), RADIUS)
                    else:
                        posX = event.pos[0]
                        pygame.draw.circle(screen, self.YELLOW, (posX, int(SQUARE_SIZE / 2)), RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, self.BLACK, (0, 0, width, SQUARE_SIZE))
                    pygame.display.update()
                    posX = event.pos[0]
                    playerChoice = int(floor(posX/SQUARE_SIZE))

                    if not self.allowsMove(playerChoice):
                        label = errorFont.render("No spaces available in column # " + str(playerChoice + 1), 1, self.RED)
                        screen.blit(label, (40, 40))
                        pygame.display.update()
                        pygame.time.wait(3000)
                    else:
                        self.addMove(playerChoice, currPlayer)

                        if self.winsFor(currPlayer):
                            self.drawBoard()

                            if currPlayer == 'X':
                                label = winFont.render("Red Wins!!", 1, self.RED)
                            else:
                                label = winFont.render("Yellow Wins!!", 1, self.YELLOW)
                            screen.blit(label, (40, 10))
                            pygame.display.update()
                            pygame.time.wait(3000)
                            runGame = False
                        else:
                            if currPlayer == 'X':
                                currPlayer = 'O'
                            else:
                                currPlayer = 'X'


b = Board()

pygame.init()
SQUARE_SIZE = 100
width = b.width * SQUARE_SIZE
height = (b.height + 1) * SQUARE_SIZE
size = (width, height)
RADIUS = int(SQUARE_SIZE/2 - 5)
screen = pygame.display.set_mode(size)
errorFont = pygame.font.SysFont("monospace", 30)
winFont = errorFont = pygame.font.SysFont("monospace", 75)

b.hostGame()






