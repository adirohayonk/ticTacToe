import computer


class Tester():

    def __init__(self, game):
        self.gameObj = game

    def testerRunner(self, numberOfGames):
        while numberOfGames > 0:
            self.randomTester()
            numberOfGames -= 1

    def randomTester(self):
        self.board, player = self.gameObj.initateGame()
        self.computerPlayer = computer.Computer(self.gameObj)
        while True:
            self.board = self.computerPlayer.computerMoveMedium(1)
            result, winningElements = self.gameObj.check_winner()
            if result is not None:
                self.gameObj.display_game()
                return
            if self.gameObj.isDraw():
                self.gameObj.display_game()
                return
            player = self.gameObj.switch_player(player)
            self.board = self.computerPlayer.computerMove("Hard")
            result, winningElements = self.gameObj.check_winner()
            if result is not None:
                self.gameObj.display_game(winningElements)
                return
            self.gameObj.display_game()
            player = self.gameObj.switch_player(player)
        exit(0)