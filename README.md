
# Tic Tac Toe Game

## Table of contents
1. [ Usage Instructions. ](#usage)
2. [ Game Options. ](#game)
3. [ Computer algorithm. ](#computer)


<a name="usage"></a>
## 1. Usage Instructions
clone the repository 
```bash
git clone https://github.com/adirohayonk/ticTacToe.git
```
run the game by
```python
python tic_tac_toe.py
```

<a name="game"></a>
## 2. Game Options
### Play against The computer

![Demo Animation](../assets/computer-game.gif?raw=true)

### Play against friend
![Demo Animation2](../assets/multi-player-game.gif?raw=true)

### Test game
![Demo Animation3](../assets/test.gif?raw=true)


<a name="computer"></a>
## 3. Computer algorithm
The computer can play in 3 different levels: Easy, Medium, Impossible.
- Easy
  - In this level the computer will choose the first empty spot and mark the X on it.
- Medium
  - In this level the computer will choose the next empty spot randomly and mark the X on it.
- Impossible
  - In this level the computer is unbeatable using this system:
    1. the computer will mark the middle if available.
    2. the computer will mark the top left upper corner if available.
    3. then the computer will use the following methods:
        - blockOrWin - This method will block the other player if possible.
        - tryToWin - this method will loop over the board and increase ranking by 1 for each box depending on the neighbors, then the computer will choose the highest rank box and mark it.
