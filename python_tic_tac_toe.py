#Imports
import IPython.display
from IPython.display import clear_output as clear
import time
import pandas as pd

jogo = pd.read_excel('C:\tabletop.xlsx')

#Funções

##Facilitadores

def stay(): #Limpa o painel e coloca um delay de 1s
  clear()
  time.sleep(1)

def tabela(): #Limpa o painel, mostra a tela atual do jogo e coloca um delay de 1s
  stay()
  print(jogo)
  print()
  time.sleep(1)

def dig_coluna(): #Pergunta qual coluna gostaria de jogar e puxa a função de validação
  coluna = input('Digite a coluna que deseja jogar (A, B ou C) \n')
  coluna = val_coluna(coluna)
  return coluna

def dig_linha(): #Pergunta qual linha gostaria de jogar e puxa a função de validação
  linha = input('Digite a linha que deseja jogar (0, 1 ou 2) \n')
  linha = val_linha(linha)
  stay()
  return linha

##Tratamento de excessão

def vazio (coluna,linha): #Valida se o local escolhido para jogar está vazio e disponível
  while jogo[coluna][int(linha)] != '-':
    tabela()
    print('O local selecionado já foi escolhido, por favor escolha outro')
    coluna = dig_coluna()
    linha = dig_linha()
  return coluna,linha

def val_coluna (coluna): #Valida se a coluna escolhida é um valor válido
  while coluna != "A" and coluna != "B" and coluna != "C":
    stay()
    print('Coluna inválida! Digite apenas "A", "B" ou "C"')
    coluna = input('Digite novamente a coluna que deseja jogar \n')
  return coluna

def val_linha (linha): #Valida se a linha escolhida é um valor válido
  while linha != "0" and linha  != "1" and linha  != "2":
    stay()
    print('linha inválida! Digite apenas "0", "1" ou "2"')
    linha = input('Digite novamente a linha que deseja jogar \n')
  return linha

##Jogada da máquina a partir da terceira rodada (Primeira deve priorizar o centro ou a borda superior direita)
def jogada ():
  #Jogar em algum lugar vazio
  if jogo['A'][1] == '-':
    coluna = 'A'
    linha = '1'
  if jogo['B'][0] == '-':
    coluna = 'B'
    linha = '0'
  if jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['B'][2] == '-':
    coluna = 'B'
    linha = '2'
  if jogo['C'][1] == '-':
    coluna = 'C'
    linha = '1'
  if jogo['A'][0] == '-':
    coluna = 'A'
    linha = '0'
  if jogo['C'][0] == '-':
    coluna = 'C'
    linha = '0'
  if jogo['A'][2] == '-':
    coluna = 'A'
    linha = '2'
  if jogo['C'][2] == '-':
    coluna = 'C'
    linha = '2'

  ##Barrar o jogador de vencer
  #Coluna A
  if jogo['A'][0] == 'O' and jogo['A'][1] == 'O' and jogo['A'][2] == '-':
    coluna = 'A'
    linha = '2'
  if jogo['A'][0] == 'O' and jogo['A'][2] == 'O' and jogo['A'][1] == '-':
    coluna = 'A'
    linha = '1'
  if jogo['A'][1] == 'O' and jogo['A'][2] == 'O' and jogo['A'][0] == '-':
    coluna = 'A'
    linha = '0'
  #Coluna B
  if jogo['B'][0] == 'O' and jogo['B'][1] == 'O' and jogo['B'][2] == '-':
    coluna = 'B'
    linha = '2'
  if jogo['B'][0] == 'O' and jogo['B'][2] == 'O' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['B'][1] == 'O' and jogo['B'][2] == 'O' and jogo['B'][0] == '-':
    coluna = 'B'
    linha = '0'
  #Coluna C
  if jogo['C'][0] == 'O' and jogo['C'][1] == 'O' and jogo['C'][2] == '-':
    coluna = 'C'
    linha = '2'
  if jogo['C'][0] == 'O' and jogo['C'][2] == 'O' and jogo['C'][1] == '-':
    coluna = 'C'
    linha = '1'
  if jogo['C'][2] == 'O' and jogo['C'][1] == 'O' and jogo['C'][0] == '-':
    coluna = 'C'
    linha = '0'
  #Linha 0
  if jogo['A'][0] == 'O' and jogo['B'][0] == 'O' and jogo['C'][0] == '-':
    coluna = 'C'
    linha = '0'
  if jogo['A'][0] == 'O' and jogo['C'][0] == 'O' and jogo['B'][0] == '-':
    coluna = 'B'
    linha = '0'
  if jogo['B'][0] == 'O' and jogo['C'][0] == 'O' and jogo['A'][0] == '-':
    coluna = 'A'
    linha = '0'
  #Linha 1
  if jogo['A'][1] == 'O' and jogo['B'][1] == 'O' and jogo['C'][1] == '-':
    coluna = 'C'
    linha = '1'
  if jogo['A'][1] == 'O' and jogo['C'][1] == 'O' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['B'][1] == 'O' and jogo['C'][1] == 'O' and jogo['A'][1] == '-':
    coluna = 'A'
    linha = '1'
  #Linha 2
  if jogo['A'][2] == 'O' and jogo['B'][2] == 'O' and jogo['C'][2] == '-':
    coluna = 'C'
    linha = '2'
  if jogo['A'][2] == 'O' and jogo['C'][2] == 'O' and jogo['B'][2] == '-':
    coluna = 'B'
    linha = '2'
  if jogo['B'][2] == 'O' and jogo['C'][2] == 'O' and jogo['A'][2] == '-':
    coluna = 'A'
    linha = '2'
  #Diagonal A
  if jogo['A'][0] == 'O' and jogo['B'][1] == 'O' and jogo['C'][2] == '-':
    coluna = 'C'
    linha = '2'
  if jogo['A'][0] == 'O' and jogo['C'][2] == 'O' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['B'][1] == 'O' and jogo['C'][2] == 'O' and jogo['A'][0] == '-':
    coluna = 'A'
    linha = '0'
  #Diagonal C
  if jogo['C'][0] == 'O' and jogo['B'][1] == 'O' and jogo['A'][2] == '-':
    coluna = 'A'
    linha = '2'
  if jogo['C'][0] == 'O' and jogo['A'][2] == 'O' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['A'][0] == 'O' and jogo['B'][1] == 'O' and jogo['C'][0] == '-':
    coluna = 'C'
    linha = '0'

  ##Tentar ganhar
  #Coluna A
  if jogo['A'][0] == 'X' and jogo['A'][1] == 'X' and jogo['A'][2] == '-':
    coluna = 'A'
    linha = '2'
  if jogo['A'][0] == 'X' and jogo['A'][2] == 'X' and jogo['A'][1] == '-':
    coluna = 'A'
    linha = '1'
  if jogo['A'][1] == 'X' and jogo['A'][2] == 'X' and jogo['A'][0] == '-':
    coluna = 'A'
    linha = '0'
  #Coluna B
  if jogo['B'][0] == 'X' and jogo['B'][1] == 'X' and jogo['B'][2] == '-':
    coluna = 'B'
    linha = '2'
  if jogo['B'][0] == 'X' and jogo['B'][2] == 'X' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['B'][1] == 'X' and jogo['B'][2] == 'X' and jogo['B'][0] == '-':
    coluna = 'B'
    linha = '0'
  #Coluna C
  if jogo['C'][0] == 'X' and jogo['C'][1] == 'X' and jogo['C'][2] == '-':
    coluna = 'C'
    linha = '2'
  if jogo['C'][0] == 'X' and jogo['C'][2] == 'X' and jogo['C'][1] == '-':
    coluna = 'C'
    linha = '1'
  if jogo['C'][1] == 'X' and jogo['C'][2] == 'X' and jogo['C'][0] == '-':
    coluna = 'C'
    linha = '0'
  #Linha 0
  if jogo['A'][0] == 'X' and jogo['B'][0] == 'X' and jogo['C'][0] == '-':
    coluna = 'C'
    linha = '0'
  if jogo['A'][0] == 'X' and jogo['C'][0] == 'X' and jogo['B'][0] == '-':
    coluna = 'B'
    linha = '0'
  if jogo['B'][0] == 'X' and jogo['C'][0] == 'X' and jogo['A'][0] == '-':
    coluna = 'A'
    linha = '0'
  #Linha 1
  if jogo['A'][1] == 'X' and jogo['B'][1] == 'X' and jogo['C'][1] == '-':
    coluna = 'C'
    linha = '1'
  if jogo['A'][1] == 'X' and jogo['C'][1] == 'X' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['B'][1] == 'X' and jogo['C'][1] == 'X' and jogo['A'][1] == '-':
    coluna = 'A'
    linha = '1'
  #Linha 2
  if jogo['A'][2] == 'X' and jogo['B'][2] == 'X' and jogo['C'][2] == '-':
    coluna = 'C'
    linha = '2'
  if jogo['A'][2] == 'X' and jogo['C'][2] == 'X' and jogo['B'][2] == '-':
    coluna = 'B'
    linha = '2'
  if jogo['B'][2] == 'X' and jogo['C'][2] == 'X' and jogo['A'][2] == '-':
    coluna = 'A'
    linha = '2'
  #Diagonal A
  if jogo['A'][0] == 'X' and jogo['B'][1] == 'X' and jogo['C'][2] == '-':
    coluna = 'C'
    linha = '2'
  if jogo['A'][0] == 'X' and jogo['C'][2] == 'X' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['B'][1] == 'X' and jogo['C'][2] == 'X' and jogo['A'][0] == '-':
    coluna = 'A'
    linha = '0'
  #Diagonal C
  if jogo['C'][0] == 'X' and jogo['B'][1] == 'X' and jogo['A'][2] == '-':
      coluna = 'A'
      linha = '2'
  if jogo['C'][0] == 'X' and jogo['A'][2] == 'X' and jogo['B'][1] == '-':
    coluna = 'B'
    linha = '1'
  if jogo['A'][2] == 'X' and jogo['B'][1] == 'X' and jogo['C'][0] == '-':
    coluna = 'C'
    linha = '0'

  return coluna,linha

##Vitória

def ganhou (): #Verifica se e quem ganhou
  vitoria = 0 #Caso não seja alterada significa que o jogo deve continuar, pois ninguém ganhou
  #A Máquina Ganhou?
  #Coluna A
  if jogo['A'][0] == 'X' and jogo['A'][1] == 'X' and jogo['A'][2] == 'X':
    vitoria = 1
  #Coluna B
  if jogo['B'][0] == 'X' and jogo['B'][1] == 'X' and jogo['B'][2] == 'X':
    vitoria = 1
  #Coluna C
  if jogo['C'][0] == 'X' and jogo['C'][1] == 'X' and jogo['C'][2] == 'X':
    vitoria = 1
  #Linha 0
  if jogo['A'][0] == 'X' and jogo['B'][0] == 'X' and jogo['C'][0] == 'X':
    vitoria = 1
  #Linha 1
  if jogo['A'][1] == 'X' and jogo['B'][1] == 'X' and jogo['C'][1] == 'X':
    vitoria = 1
  #Linha 2
  if jogo['A'][2] == 'X' and jogo['B'][2] == 'X' and jogo['C'][2] == 'X':
    vitoria = 1
  #Diagonal A
  if jogo['A'][0] == 'X' and jogo['B'][1] == 'X' and jogo['C'][2] == 'X':
    vitoria = 1
  #Diagonal C
  if jogo['C'][0] == 'X' and jogo['B'][1] == 'X' and jogo['A'][2] == 'X':
    vitoria = 1

  #O jogador ganhou?
  #Coluna A
  if jogo['A'][0] == 'O' and jogo['A'][1] == 'O' and jogo['A'][2] == 'O':
    vitoria = 2
  #Coluna B
  if jogo['B'][0] == 'O' and jogo['B'][1] == 'O' and jogo['B'][2] == 'O':
    vitoria = 2
  #Coluna C
  if jogo['C'][0] == 'O' and jogo['C'][1] == 'O' and jogo['C'][2] == 'O':
    vitoria = 2
  #Linha 0
  if jogo['A'][0] == 'O' and jogo['B'][0] == 'O' and jogo['C'][0] == 'O':
    vitoria = 2
  #Linha 1
  if jogo['A'][1] == 'O' and jogo['B'][1] == 'O' and jogo['C'][1] == 'O':
    vitoria = 2
  #Linha 2
  if jogo['A'][2] == 'O' and jogo['B'][2] == 'O' and jogo['C'][2] == 'O':
    vitoria = 2
  #Diagonal A
  if jogo['A'][0] == 'O' and jogo['B'][1] == 'O' and jogo['C'][2] == 'O':
    vitoria = 2
  #Diagonal C
  if jogo['C'][0] == 'O' and jogo['B'][1] == 'O' and jogo['A'][2] == 'O':
    vitoria = 2

  #Resultado
  if vitoria == 1:
    print("Que pena! Você perdeu!")
  if vitoria == 2:
    print("Parabéns! Você ganhou!")
  return vitoria

#Código Principal

#jogo em branco
jogo = pd.read_excel('C:\tabletop.xlsx')
tabela()

#Quem começa?
resp = input("Você gostaria de começar? S/N \n")
while resp.upper() != "S" and resp.upper() != "N":
  stay()
  print('Resposta inválida! Digite apenas "S" ou "N"')
  resp = input("Você gostaria de começar? S/N \n")
stay()


#Código se a máquina começar
if resp == 'N':

  #Primeira Rodada
  print("Vez da máquina!")
  jogo['B'][1] = 'X'
  tabela()

  #Segunda Rodada
  print("Sua vez!")
  coluna = dig_coluna()
  linha = dig_linha()

  coluna, linha = vazio(coluna,linha)

  jogo[coluna][int(linha)] = 'O'
  tabela()

  #Terceira Rodada
  print("Vez da máquina!")
  if jogo['A'][0] == '-':
    jogo['A'][0] = 'X'
  else:
    jogo['A'][2] = 'X'
  tabela()

  #Quarta Rodada
  print("Sua vez!")
  coluna = dig_coluna()
  linha = dig_linha()

  coluna, linha = vazio(coluna,linha)

  jogo[coluna][int(linha)] = 'O'
  tabela()

  #Quinta Rodada
  print("Vez da máquina!")
  coluna,linha = jogada()
  jogo[coluna][int(linha)] = 'X'
  tabela()

  #Sexta Rodada
  vitoria = ganhou()
  if vitoria == 0:
    print("Sua vez!")
    coluna = dig_coluna()
    linha = dig_linha()

    coluna, linha = vazio(coluna,linha)

    jogo[coluna][int(linha)] = 'O'
    tabela()

  #Sétima Rodada
    vitoria = ganhou()
    if vitoria == 0:
      print("Vez da máquina!")
      coluna,linha = jogada()
      jogo[coluna][int(linha)] = 'X'
      tabela()

  #Oitava Rodada
      vitoria = ganhou()
      if vitoria == 0:
        print("Sua vez!")
        coluna = dig_coluna()
        linha = dig_linha()

        coluna, linha = vazio(coluna,linha)

        jogo[coluna][int(linha)] = 'O'
        tabela()

  #Nona/Ultima Rodada
        vitoria = ganhou()
        if vitoria == 0:
          print("Vez da máquina!")
          coluna,linha = jogada()
          jogo[coluna][int(linha)] = 'X'
          tabela()
        vitoria = ganhou()
        if vitoria == 0:
          print("Declarado empate!")

#Código se o jogador começar
if resp == 'S':

  #Primeira Rodada
  tabela()
  print("Sua vez!")
  coluna = dig_coluna()
  linha = dig_linha()

  jogo[coluna][int(linha)] = 'O'
  tabela()

  #Segunda Rodada
  stay()
  print("Vez da máquina!")
  if jogo['B'][1] == '-':
    jogo['B'][1] = 'X'
    tabela()
  else:
    jogo['C'][0] = 'X'
    tabela()

  #Terceira Rodada
  print("Sua vez!")
  coluna = dig_coluna()
  linha = dig_linha()

  jogo[coluna][int(linha)] = 'O'
  tabela()

  #Quarta Rodada
  print("Vez da máquina!")
  coluna,linha = jogada()
    #Tratamento de jogadas específicas
  if jogo['C'][0] == 'O' and jogo['A'][2] == 'O':
    coluna = 'B'
    linha = '2'
  if jogo['A'][0] == 'O' and jogo['C'][2] == 'O':
    coluna = 'B'
    linha = '2'

  if jogo['C'][1] == 'O' and jogo['A'][0] == 'O':
    coluna = 'C'
    linha = '0'
  if jogo['A'][1] == 'O' and jogo['C'][0] == 'O':
    coluna = 'A'
    linha = '02'

  jogo[coluna][int(linha)] = 'X'
  tabela()

  #Quinta Rodada
  print("Sua vez!")
  coluna = dig_coluna()
  linha = dig_linha()

  coluna, linha = vazio(coluna,linha)

  jogo[coluna][int(linha)] = 'O'
  tabela()

  #Sexta Rodada
  vitoria = ganhou()
  if vitoria == 0:
    print("Vez da máquina!")
    coluna,linha = jogada()
    jogo[coluna][int(linha)] = 'X'
    tabela()

  #Sétima Rodada
    vitoria = ganhou()
    if vitoria == 0:
      print("Sua vez!")
      coluna = dig_coluna()
      linha = dig_linha()

      coluna, linha = vazio(coluna,linha)

      jogo[coluna][int(linha)] = 'O'
      tabela()

  #Oitava Rodada
      vitoria = ganhou()
      if vitoria == 0:
        print("Vez da máquina!")
        coluna,linha = jogada()
        jogo[coluna][int(linha)] = 'X'
        tabela()

  #Nona Rodada
        vitoria = ganhou()
        if vitoria == 0:
          print("Sua vez!")
          coluna = dig_coluna()
          linha = dig_linha()

          coluna, linha = vazio(coluna,linha)

          jogo[coluna][int(linha)] = 'O'
          tabela()
