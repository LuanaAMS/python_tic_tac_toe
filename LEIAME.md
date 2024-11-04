<a href="https://github.com/LuanaAMS/python_tic_tac_toe/blob/main/README.md" target="_blank"> English Version </a>

![Badge Finalizado](http://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=GREEN&style=for-the-badge)

# Python - Tic Tac Toe (Jogo da Velha)

Este projeto é um tic tac toe (Jogo da Velha) feito em Python que usa uma estratégia simples para sempre tentar vencer o jogador.

## O que é um TIC TAC TOE (Jogo da Velha)?

O jogo é jogado em um tabuleiro 3x3, onde dois jogadores se revezam para colocar seu símbolo (X ou O) em uma célula vazia. O jogador que primeiro conseguir três de seus símbolos em sequência (horizontalmente, verticalmente ou diagonalmente) ganha o jogo.

Neste programa, o jogador sempre jogará com o símbolo 'O'. Mas ele pode escolher se quer ou não começar. Se o jogador escolher começar, a máquina terá um código mais complexo. Se o jogador escolher não começar, o código é menor e mais simples. Em ambas as escolhas a máquina tem mais chance de vencer. 

## Qual é a estratégia?

A máquina usa uma estratégia simples que consiste em:

  - Verificar se pode vencer na próxima jogada. Se sim, fazer essa jogada.

  - Se não puder vencer na próxima jogada, verificar se o jogador pode vencer na próxima jogada. Se sim, bloquear essa jogada.

  - Se não puder vencer nem bloquear o jogador na próxima jogada, fazer qualquer jogada que ainda lhe dê chances de vencer.

Vale ressaltar que todas as decisões da máquina foram feitas usando apenas o recurso de gateway "IF", além de ter seus blocos de código organizados por "DEF".

## Requisitos:
- Python 3.8 ou superior
- Bibliotecas "pandas", "IPython" e "time"

## Como jogar:

Você pode acessar o projeto de forma local por meio dessas etapas:

- Clone o repositório do GitHub

- Faça Download do arquivo "tabletop.xlsx", localizado neste repositório.

- Instale as dependências no CMD:

    'pip install ipython'

    'pip install pandas'

- Substitua na linha 7 e linha 321 o 'C:\tabletop.xlsx' pelo local em que baixou o arquivo "tabletop.xlsx".

- Execute o jogo

Além disso, poderá rodar pelo navegador utilizando o Google Colaboratory  por meio desse passo a passo:

- Acesse o seguinte link: [Colaboratory-Jogo-da-Velha](https://colab.research.google.com/drive/1BbpGoDwUy2H_ui6IfMLb6VZL4Bof6n3_?usp=sharing)
  
- Vá em "Arquivo" e em seguida "Salvar uma cópia no Drive"

- Faça Download do arquivo "tabletop.xlsx", localizado neste repositório.

- Na barra esquerda do Colaboratory, selecione o símbolo de pasta e após isso o Primeiro ícone (um papel com uma seta para cima).

- Faça upload do arquivo "tabletop.xlsx" por meio deste ícone

- Execute a célula "Código Principal"

## Contribuições:
Contribuições são bem-vindas. Para contribuir, envie um e-mail para luana.ams04@gmail.com

## Licença:
Este projeto é licenciado sob a licença MIT.


<a href="https://github.com/LuanaAMS/python_tic_tac_toe/blob/main/README.md" target="_blank"> English Version </a>
