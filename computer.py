import random


class Computer():
    def __init__(self, game):
        self.gameObj = game
        self.board = self.gameObj.gameBoard
        self.computerTurnNumber = 1

    def computerMoveEasy(self):
        for row in range(3):
            for column in range(3):
                if self.gameObj.check_spot(row, column, printLog=False):
                    self.board = self.gameObj.add_piece(2, row, column)
                    return self.board

    def computerMoveMedium(self, playerNumber):
        positions = [(x, y) for x in range(3) for y in range(3)]
        while True:
            row, column = random.choice(positions)
            if self.gameObj.check_spot(row, column, printLog=False):
                self.board = self.gameObj.add_piece(playerNumber, row, column)
                return self.board
            else:
                positions.remove((row, column))
            if len(positions) == 0:
                return self.board

    def blockOrWin(self):
        winRow, winCol = -1, -1
        isWinner = False
        for row in range(len(self.board)):
            for column in range(len(self.board)):
                if self.board[row][column] == 0:
                    self.board[row][column] = 2
                    winner, _ = self.gameObj.check_winner(printWinner=False)
                    if winner is not None:
                        winRow, winCol = row, column
                        isWinner = True
                    self.board[row][column] = 1
                    winner, _ = self.gameObj.check_winner(printWinner=False)
                    if winner is not None:
                        if not(isWinner):
                            winRow, winCol = row, column
                    self.board[row][column] = 0
        if isWinner:
            self.board[winRow][winCol] = 2
            self.board = self.gameObj.add_piece(2, winRow, winCol)
            return True, self.board
        elif winRow != -1:
            self.board = self.gameObj.add_piece(2, winRow, winCol)
            return True, self.board
        return False, self.board

    def checkDiag(self, diagPoints):
        elementsInDiagonal = list()
        elementsPoints = list()
        for point in diagPoints:
            elementsInDiagonal.append(self.board[point[0]][point[1]])
            elementsPoints.append((point[0], point[1]))
        if elementsInDiagonal[0] == 0:
            if elementsInDiagonal[1] == 2 and elementsInDiagonal[2] == 1:
                self.board = self.gameObj.add_piece(2, elementsPoints[0][0],
                                                    elementsPoints[0][1])
                return True, self.board

        if elementsInDiagonal[2] == 0:
            if elementsInDiagonal[1] == 2 and elementsInDiagonal[0] == 1:
                self.board = self.gameObj.add_piece(2, elementsPoints[2][0],
                                                    elementsPoints[2][1])
                return True, self.board
        return False, self.board

    def tryToWin(self):
        rowToCheck = list()
        winPosX, winPosY = 0, 0
        currentRanking = 0
        winningOptions = list()
        winPosExist = False
        mainDiag = self.gameObj.winningPosition[6]
        secondDiag = self.gameObj.winningPosition[7]
        diagPlayed, self.board = self.checkDiag(mainDiag)
        if diagPlayed:
            return diagPlayed, self.board
        diagPlayed, self.board = self.checkDiag(secondDiag)
        if diagPlayed:
            return diagPlayed, self.board
        for rowElem in range(len(self.gameObj.winningPosition)):
            currWinningPos = self.gameObj.winningPosition[rowElem]
            for pos in currWinningPos:
                posX, posY = pos
                if self.board[posX][posY] == 1:
                    break
                if self.board[posX][posY] == 0:
                    posRank = self.gameObj.ranking[(posX, posY)]
                    if posRank >= currentRanking:
                        currentRanking = posRank
                        winPosX, winPosY = posX, posY
                    rowToCheck.append(2)
                if self.board[posX][posY] == 2:
                    rowToCheck.append(2)
            if len(rowToCheck) == 3:
                if self.gameObj.check_row_winner(rowToCheck) != 0:
                    winningOptions.append((winPosX, winPosY, currentRanking))
                    winPosExist = True
            winPosX, winPosY = 0, 0
            currentRanking = 0
            rowToCheck = list()
        biggestRank = 0
        for winOpt in winningOptions:
            if winOpt[2] >= biggestRank:
                winPosX = winOpt[0]
                winPosY = winOpt[1]
                biggestRank = winOpt[2]
        if winPosExist:
            self.board = self.gameObj.add_piece(2, winPosX, winPosY)
            return winPosExist, self.board
        return False, self.board

    def computerMoveImpossible(self):
        if self.computerTurnNumber == 1:
            if self.board[1][1] == 0:
                self.gameObj.add_piece(2, 1, 1)
                return self.board
            elif self.board[0][0] == 0:
                self.gameObj.add_piece(2, 0, 0)
                return self.board
        isPlayed, self.board = self.blockOrWin()
        if not(isPlayed):
            isPlayed, self.board = self.tryToWin()
        return self.board

    def computerMove(self, level):
        if level == "Easy":
            self.board = self.computerMoveEasy()
        if level == "Medium":
            self.board = self.computerMoveMedium(2)
        if level == "IMPOSSIBLE":
            self.board = self.computerMoveImpossible()
        self.computerTurnNumber += 1
        return self.board
