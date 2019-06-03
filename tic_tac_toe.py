import argparse
import random
import os
import game
import tester
import computer


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

    numberOfPlayers = int(input("How many players "))
    if numberOfPlayers == 2:
        gameObj.multiPlayerGame()
    elif numberOfPlayers == 1:
        gameObj.singlePlayerGame()

if __name__ == '__main__':
    main()
