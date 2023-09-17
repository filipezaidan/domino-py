import os
import random
from time import sleep
from domino import Piece
from typing import List

def generatePieces(): # Gera as peças do dominó
  pieces: List[Piece] = []

  for count in range(7):
    for max in range(count, 7):
      piece = Piece(count,max)
      pieces.append(piece)

  loading('Gerando as peças')

  sleep(0.5) # Delay
  cls() # Limpa o terminal

  return pieces

def sortPieces(pieces: List[Piece]): # Sortear as peças do dominó
  loading('Embaralhando as peças')

  sleep(1) 
  cls()

  piecesSorted = pieces
  random.shuffle(piecesSorted) # Embaralha as peças

  print('Peças embaralhadas com sucesso!')

  sleep(1)
  cls()
  return piecesSorted

def cls(): # Limpa o terminal
  os.system('cls')


def loading(text):
    cls() # Limpa o terminal
    ret = '.'
    count = 0

    while count < 6:
      print(text + ret) # Loading.

      if len(ret) < 3:
        ret += '.'
      else:
        ret = '.'

      count += 1
      sleep(0.3)
      cls()

    sleep(0.5) # Para parecer que está carregando...
    cls() # Limpa o terminal (Carregou kkkkkk)