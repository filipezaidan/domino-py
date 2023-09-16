import random
from time import sleep
from domino import Piece
from typing import List

#Gera as peças do dominó
def generatePieces():
  pieces: List[Piece] = []

  for count in range(7):
    for max in range(count, 7):
      piece = Piece(count,max)
      pieces.append(piece)

  print('Gerando peças ...')
  sleep(1)
  return pieces

# Sortear as peças do dominó
def sortPieces(pieces: List[Piece]):
  print('Embaralhando as peças ...')
  sleep(2)
  piecesSorted = pieces
  random.shuffle(piecesSorted)

  print('Peças embaralhadas com sucesso!')
  return piecesSorted