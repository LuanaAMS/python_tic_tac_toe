<a href="https://github.com/LuanaAMS/python_tic_tac_toe/blob/main/LEIAME.md" target="_blank"> PT-BR Version </a>


![Badge Complete](http://img.shields.io/static/v1?label=STATUS&message=COMPLETE&color=GREEN&style=for-the-badge)


# Python - Tic Tac Toe
This project is a tic-tac-toe game made in Python and Pandas that uses a simple strategy to always try to beat the player.

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

You can access the project locally through these steps:

- Clone the GitHub repository.
  
- Download the "tabletop.xlsx" file located in this repository.
  
- Install the dependencies in CMD:

    'pip install ipython'
  
    'pip install pandas'

- Replace 'C:\tabletop.xlsx' with the location where you downloaded the "tabletop.xlsx" file on line 7 and line 321.

 - Execute the game.

Additionally, you can run it through the browser using Google Colaboratory by following these steps:

- Access the following link: [Colaboratory-Tic-Tac-Toe](https://colab.research.google.com/drive/1BbpGoDwUy2H_ui6IfMLb6VZL4Bof6n3_?usp=sharing)

- Go to "File" and then "Save a copy in Drive".

- Download the "tabletop.xlsx" file located in this repository.

- In the left bar of Colaboratory, select the folder symbol and then the first icon (a paper with an arrow pointing up).

- Upload the "tabletop.xlsx" file through this icon.

- Execute the "Código Principal" cell.

## Contributions:

Contributions are welcome. To contribute, send an email to luana.ams04@gmail.com

## License:

This project is licensed under the MIT License.

<a href="https://github.com/LuanaAMS/python_tic_tac_toe/blob/main/LEIAME.md" target="_blank"> PT-BR Version </a>
