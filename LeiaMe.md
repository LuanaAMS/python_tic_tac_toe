Este projeto é um tic tac toe feito em Python que usa uma estratégia simples para sempre tentar vencer o jogador.

## What is TIC TAC TOE?

O jogo é jogado em um tabuleiro 3x3, onde dois jogadores se revezam para colocar seu símbolo (X ou O) em uma célula vazia. O jogador que primeiro conseguir três de seus símbolos em sequência (horizontalmente, verticalmente ou diagonalmente) ganha o jogo.

Neste programa, o jogador sempre jogará com o símbolo 'O'. Mas ele pode escolher se quer ou não começar. Se o jogador escolher começar, a máquina terá um código mais complexo. Se o jogador escolher não começar, o código é menor e mais simples. Em ambas as escolhas a máquina tem mais chance de vencer. 

## Qual é a estratégia?

A máquina usa uma estratégia simples que consiste em:

  - Verificar se pode vencer na próxima jogada. Se sim, fazer essa jogada.

  - Se não puder vencer na próxima jogada, verificar se o jogador pode vencer na próxima jogada. Se sim, bloquear essa jogada.

  - Se não puder vencer nem bloquear o jogador na próxima jogada, fazer qualquer jogada que ainda lhe dê chances de vencer.

Vale ressaltar que todas as decisões da máquina foram feitas usando apenas o recurso de gateway "IF", além de ter seus blocos de código organizados por "DEF".

## Requisitos:
Python 3.8 ou superior
Bibliotecas "pandas", "IPython" and "time"

## Como jogar:
Você pode acessar o jogo pelo Google Colaboratory nesse link:
https://colab.research.google.com/drive/1b-41NmC9K2dhTPPwyKrAs54C8h7IsYbV?usp=sharing

Além disso, pode seguir estas etapas para rodar localmente:

  - Clone o repositório do GitHub
  - Faça Download do arquivo "tabletop.xlsx", localizado neste repositório.
  - Instale as dependências no CMD:
    pip install ipython
    pip install pandas
  - Substitua na linha 7 e linha 325 o '/content/drive/MyDrive/Colab Notebooks/#.xlsx' pelo arquivo "tabletop.xlsx".
  - Execute o jogo

## Contribuições:
Contribuições são bem-vindas. Para contribuir, envie um e-mail para luana.ams04@gmail.com

## Licença:
Este projeto é licenciado sob a licença MIT.
