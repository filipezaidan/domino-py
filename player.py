from lista import ListHandsPieces
from domino import Piece, PieceNode

class Player:
    def __init__(self, name):
        self.name = name
        self._mypieces:ListHandsPieces = None

    def __repr__(self):
        pass


    def getQtdPieces(self):
        return self._mypieces.size()

    def getPecas(self, pieces):
        self._mypieces = pieces

    def showMyHands(self):
        atual = self._mypieces.head
        str = ''
        count = 0
        while atual != None:
            count+=1
            str+= '(%s) -> [%s|%s] \n' % (count, atual.piece.left, atual.piece.right)
            atual = atual.getNext()
        return print(str + '(0) -> Passar a vez')

    def searchPiece(self, opcao: int):
        mypieces = self._mypieces
        atual: PieceNode = mypieces.head
        encontrou: bool = False
        count: int = 1
        piece = None
        
        while atual is not None and not encontrou:
            if opcao == count:
                encontrou = True
                piece = atual.piece
            else:
                count += 1
                atual = atual.getNext()
        if encontrou:
            return piece
        else:
            print('Opção inválida!')
            return None


    def removePiece(self, indice: int) -> int:
        mypieces = self._mypieces
        atual: PieceNode = mypieces.head
        anterior: PieceNode = None
        encontrou: bool = False
        count: int = 1

        while atual is not None and not encontrou:
            if indice == count:
                encontrou = True
            else:
                count += 1
                anterior = atual
                atual = atual.getNext()

        if encontrou:
            if anterior is None:
                mypieces.head = atual.getNext()
            else:
                anterior.setNext(atual.getNext())

            self._mypieces = mypieces

        else:
            print('Peça não encontrada no índice especificado.')
    
    def countPoints(self):
        atual = self._mypieces.head
        points = 0
        while atual != None:
            points+= atual.piece.getPoints()
            atual = atual.getNext()
        return points

        