import argparse
import game
import tester


def readInt(Question):
    verify = False
    result = 0
    while not(verify):
        try:
            result = int(input(Question))
            verify = True
        except ValueError:
            print("Wrong Value")
    return result


def main():
    parser = argparse.ArgumentParser("Tic Tac Toe game")
    parser.add_argument('-t', '--tester', type=int, metavar="[Num of tests]",
                        help="Random tester against Hard computer")
    args = parser.parse_args()

    gameObj = game.Game()

    if args.tester:
        testerObj = tester.Tester(gameObj)
        testerObj.testerRunner(args.tester)
        exit(0)

    numberOfPlayers = readInt("How many players: ")
    if numberOfPlayers == 2:
        gameObj.multiPlayerGame()
    elif numberOfPlayers == 1:
        computerLevel = readInt("Level(1:Hard, 2:Medium, 3:Easy, Default:Easy:")
        gameObj.singlePlayerGame(computerLevel)


if __name__ == '__main__':
    main()
