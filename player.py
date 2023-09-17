from lista import ListHandsPieces
from domino import PieceNode

class Player: # Classe do jogador
    def __init__(self, name): # Construtor
        self.name = name
        self._mypieces:ListHandsPieces = None

    def sizePieces(self): # Retorna quantas peças o jogador tem
        return self._mypieces.size()

    def addPieces(self, pieces): # Adiciona a mão do jogador
        self._mypieces = pieces

    def showPieces(self): # Mostra a mão do jogador
        atual = self._mypieces.head
        str = ''
        count = 0
        while atual != None:
            count+=1
            str+= '(%s) -> [%s|%s] \n' % (count, atual.piece.left, atual.piece.right)
            atual = atual.getNext()
        return print(str + '(0) -> Passar a vez')
    
    def search(self, piece: int):  # Retorna se existe uma peça na mão do jogador
        pieces = self._mypieces
        current: PieceNode = pieces.head
        hasFound = False
        count: int = 1
        pieceFound = None

        while current is not None and not hasFound: # Procura a peça
            if piece == count:
                hasFound = True
                pieceFound = current.piece
            else:
                count += 1
                current = current.getNext()

        return pieceFound if hasFound else None

    def searchPiece(self, option: int): # Procura uma peça na mão do jogador e retorna ela se achar
        piece = self.search(option)

        if piece:
            return piece
        else:
            print('Opção inválida!')
            return None


    def removePiece(self, index: int): # Remove uma peça da mão do jogador
        pieces = self._mypieces
        current: PieceNode = pieces.head
        previous: PieceNode = None
        hasFound = False
        count = 1

        while current is not None and not hasFound: # Procura a peça
            if index == count:
                hasFound = True
            else:
                count += 1
                previous = current
                current = current.getNext()

        if hasFound: # Caso tenha achado a peça
            if previous is None:
                pieces.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            self._mypieces = pieces
        else: # Se não achar a peça, mostra que não encontrou
            print('Peça não encontrada.')
    
    def countPoints(self): # Conta os pontos na mão do jogador
        currentPiece = self._mypieces.head
        points = 0

        while currentPiece != None:
            points+= currentPiece.piece.getPoints()
            currentPiece = currentPiece.getNext()

        return points

        