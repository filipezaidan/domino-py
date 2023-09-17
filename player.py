from lista import ListHandsPieces
from domino import PieceNode

class Player:
    def __init__(self, name):
        self.name = name
        self._mypieces:ListHandsPieces = None

    def sizePieces(self):
        return self._mypieces.size()

    def addPieces(self, pieces):
        self._mypieces = pieces

    def showPieces(self):
        atual = self._mypieces.head
        str = ''
        count = 0
        while atual != None:
            count+=1
            str+= '(%s) -> [%s|%s] \n' % (count, atual.piece.left, atual.piece.right)
            atual = atual.getNext()
        return print(str + '(0) -> Passar a vez')
    
    def search(self, opcao:int):
        pieces = self._mypieces
        current: PieceNode = pieces.head
        isFind = False
        count: int = 1
        pieceFinded = None

        while current is not None and not isFind:
            if opcao == count:
                isFind = True
                pieceFinded = current.piece
            else:
                count += 1
                current = current.getNext()
        return pieceFinded if isFind else None

    def searchPiece(self, opcao: int):
        piece = self.search(opcao)

        if piece:
            return piece
        else:
            print('Opção inválida!')
            return None


    def removePiece(self, indice: int):
        pieces = self._mypieces
        current: PieceNode = pieces.head
        previous: PieceNode = None
        isFind = False
        count = 1

        while current is not None and not isFind:
            if indice == count:
                isFind = True
            else:
                count += 1
                previous = current
                current = current.getNext()

        if isFind:
            if previous is None:
                pieces.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            self._mypieces = pieces
        else:
            print('Peça não encontrada.')
    
    def countPoints(self):
        currentPiece = self._mypieces.head
        points = 0
        while currentPiece != None:
            points+= currentPiece.piece.getPoints()
            currentPiece = currentPiece.getNext()
        return points

        