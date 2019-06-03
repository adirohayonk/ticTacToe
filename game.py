import computer
import os


class Game():
    def __init__(self):
        self.winningPosition = {0: [(0, 0), (0, 1), (0, 2)],
                                1: [(0, 0), (1, 0), (2, 0)],
                                2: [(1, 0), (1, 1), (1, 2)],
                                3: [(0, 1), (1, 1), (2, 1)],
                                4: [(2, 0), (2, 1), (2, 2)],
                                5: [(0, 2), (1, 2), (2, 2)],
                                6: [(0, 0), (1, 1), (2, 2)],
                                7: [(0, 2), (1, 1), (2, 0)]}
        self.ranking = {(x, y): 0 for x in range(3) for y in range(3)}

    def display_winner(self, player):
        if player != 0:
            print("Player " + str(player) + " wins!")

    def updateRanking(self, possibleNeighbors, upperLimit, lowerLimit):
        for neighbor in possibleNeighbors:
            row = neighbor[0]
            column = neighbor[1]
            if row < upperLimit and row >= lowerLimit:
                if column < upperLimit and column >= lowerLimit:
                    self.ranking[(row, column)] += 1

    def updateNeighbors(self, row, column):
        upperLimit = 3
        lowerLimit = 0
        possibleNeighbors = list()
        possibleNeighbors.append((row+1, column))
        possibleNeighbors.append((row, column+1))
        possibleNeighbors.append((row+1, column+1))
        possibleNeighbors.append((row-1, column))
        possibleNeighbors.append((row, column-1))
        possibleNeighbors.append((row-1, column-1))
        possibleNeighbors.append((row+1, column-1))
        possibleNeighbors.append((row-1, column+1))
        self.updateRanking(possibleNeighbors, upperLimit, lowerLimit)

    def check_row_winner(self, row):
        """
            Return the player number that wins for that row.
            If there is no winner, return 0.
        """
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]
        return 0

    def get_col(self, col_number):
        return [self.gameBoard[x][col_number] for x in range(3)]

    def get_row(self, row_number):
        return self.gameBoard[row_number]

    def isDraw(self):
        for row in range(len(self.gameBoard)):
            for column in range(len(self.gameBoard)):
                if self.gameBoard[row][column] == 0:
                    return False
        print("It's a draw")
        return True

    def check_winner(self, printWinner=True):
        game_slices = []
        for index in range(3):
            game_slices.append(self.get_row(index))
            game_slices.append(self.get_col(index))

        # check diagonals
        down_diagonal = [self.gameBoard[x][x] for x in range(3)]
        up_diagonal = [self.gameBoard[0][2], self.gameBoard[1][1],
                       self.gameBoard[2][0]]
        game_slices.append(down_diagonal)
        game_slices.append(up_diagonal)
        for index, game_slice in enumerate(game_slices):
            winner = self.check_row_winner(game_slice)
            if winner != 0:
                if printWinner:
                    self.display_winner(winner)
                return winner, self.winningPosition[index]
        return None, None

    def start_game(self):
        return [[0, 0, 0] for x in range(3)]

    def colorText(self, text):
        if os.name == 'nt':
            import colorama
            colorama.init()
            redColor = colorama.Fore.RED
            resetColors = colorama.Style.RESET_ALL
            coloredText = f'{redColor} {text} {resetColors}'
            coloredText = " " + coloredText + " "
        else:
            CSI = "\x1B["
            coloredText = CSI + "31;40m" + text + CSI + "0m"
            coloredText = "  " + coloredText + "  "
        return coloredText

    def display_game(self, winnningPos=[]):
        symbols = {2: "O", 1: "X", 0: " "}
        lineLength = 19
        game_string = []
        for row_num in range(3):
            new_row = []
            for col_num in range(3):
                playerInPos = self.gameBoard[row_num][col_num]
                if playerInPos == 0:
                    new_row.append("({},{})".format(row_num+1, col_num+1))
                else:
                    if (row_num, col_num) in winnningPos:
                        coloredSymbol = self.colorText(symbols[playerInPos])
                        new_row.append(coloredSymbol)
                    else:
                        new_row.append("  " + symbols[playerInPos] + "  ")
            game_string.append(new_row)
        count = 0
        for game_line in game_string:
            line = ",".join(game_line)
            line = "|{}|".format(line)
            if count == 0:
                print("-" * lineLength)
            count += 1
            print(line)
        print("-" * lineLength)

    def add_piece(self, player, row, column):
        """
        game: game state
        player: player number
        row: 0-index row
        column: 0-index column
        """
        self.gameBoard[row][column] = player
        if player == 1:
            self.updateNeighbors(row, column)
        return self.gameBoard

    def convert_input_to_coordinate(self, user_input):
        return user_input - 1

    def switch_player(self, player):
        if player == 1:
            return 2
        else:
            return 1

    def check_spot(self, row, column, printLog=True):
        if self.gameBoard[row][column] != 0:
            if printLog:
                print("Wrong spot please choose an empty spot")
            return False
        return True

    def playerTurn(self, player):
        spotStatus = False
        while not(spotStatus):
            try:
                row = self.convert_input_to_coordinate(
                    int(input("(player {}) - Which row? (start with 1) "
                              .format(player))))
                column = self.convert_input_to_coordinate(
                    int(input("(player {}) - Which column? (start with 1) "
                              .format(player))))
                if row >= 0 and row < 3 and column >= 0 and column < 3:
                    spotStatus = self.check_spot(row, column)
                    self.gameBoard = self.add_piece(player, row, column)
                else:
                    print("Wrong move please choose between 1 to 3")
            except EOFError:
                exit(0)
            except:
                print("[E]Wrong move please choose between 1 to 3")

        return self.gameBoard

    def initateGame(self):
        self.gameBoard = self.start_game()
        self.display_game()
        player = 1

        for i in self.ranking:
            self.ranking[i] = 0
        return self.gameBoard, player

    def newGame(self, gameType):
        newGame = input("New game(Y, N)?:")
        if newGame in ['Y', 'y', 'yes', 'Yes', 'YES']:
            if gameType == "single":
                self.singlePlayerGame()
            else:
                self.multiPlayerGame()
        else:
            exit(0)

    def multiPlayerGame(self):
        self.gameBoard, player = self.initateGame()
        # go on forever
        while True:
            self.gameBoard = self.playerTurn(player)
            result, winningElements = self.check_winner()
            if result is not None:
                self.display_game(winningElements)
                self.newGame("multi")
            if self.isDraw():
                self.newGame("multi")
            self.display_game()
            player = self.switch_player(player)

    def singlePlayerGame(self):
        self.gameBoard, player = self.initateGame()
        computerPlayer = computer.Computer(self)
        while True:
            self.gameBoard = self.playerTurn(player)
            result, winningElements = self.check_winner()
            if result is not None:
                self.display_game(winningElements)
                self.newGame("single")
            if self.isDraw():
                self.display_game()
                self.newGame("single")
            player = self.switch_player(player)
            self.gameBoard = computerPlayer.computerMove("Hard")
            result, winningElements = self.check_winner()
            if result is not None:
                self.display_game(winningElements)
                self.newGame("single")
            self.display_game()
            player = self.switch_player(player)
