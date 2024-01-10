# python_tic_tac_toe
This project is a tic-tac-toe game made in Python that uses a simple strategy to always try to beat the player.

## What is Tic-Tac-Toe?

The game is played on a 3x3 board, where two players take turns placing their symbol (X or O) in an empty cell. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.

In this program, the player always plays as the symbol 'O'. However, they can choose whether or not to start. If the player chooses to start, the computer will have a more complex code. If the player chooses not to start, the code is smaller and simpler. In both cases, the computer has a higher chance of winning.

## What is the strategy?

The computer uses a simple strategy that consists of:

  Checking if it can win on the next move. If so, making that move.
    - If it cannot win on the next move, checking if the player can win on the next move. If so, blocking that move.
    - If it cannot win or block the player on the next move, making any move that still gives it a chance to win.
    - It is worth noting that all of the computer's decisions were made using only the "IF" gateway, in addition to having its code blocks organized by "DEF".

## Requirements:

- Python 3.8 or higher
- Libraries "pandas", "IPython", and "time"

## How to play:

You can access the game through Google Colaboratory at this link:

https://colab.research.google.com/drive/1b-41NmC9K2dhTPPwyKrAs54C8h7IsYbV?usp=sharing

Additionally, you can follow these steps to run locally:

  - Clone the GitHub repository
    
  - Install Python

  - Download the file "tabletop.xlsx" from the repository.

  - Install the dependencies in the CMD:

    pip install ipython
    
    pip install pandas

  - Replace the lines 7 and 325 with the path to the local file "tabletop.xlsx".

  - Run the game

## Contributions:

Contributions are welcome. To contribute, send an email to luana.ams04@gmail.com

## License:

This project is licensed under the MIT License.

