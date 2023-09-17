class Piece:
  def __init__(self, left:int, right:int):
    self.left = left
    self.right = right

  def __str__(self):
    return f'[{self.left}|{self.right}]'

  def invert(self):
      temp = self.left
      self.left = self.right
      self.right = temp
  
  def getPoints(self):
      return self.left + self.right

class PieceNode:
    def __init__(self, piece: Piece):
        self.piece = piece
        self.next = None

    def __repr__(self):
        if self.next is not None:
            return '[%s|%s]  %s' % (self.piece.left, self.piece.right, self.next)
        else:
            return '[%s|%s]' % (self.piece.left, self.piece.right)

    def getData(self):
        return self.piece
    
    def getNext(self):
        return self.next
    
    def setData(self, new_piece):
        self.piece = new_piece

    def setNext(self, new_next):
        self.next = new_next

class  ListPieces:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return str(self.head)

    def is_empty(self):
        return self.head == None

    def add(self,piece:Piece):
        pieceTemp = PieceNode(piece)
        isAdded = True
        if self.is_empty():
            # caso lista domino vazia
            pieceTemp.next = self.head
            self.head = self.tail = pieceTemp

        else:
            # se tiver cheia entra aqui
            firstPiece = self.head.piece
            lastPiece = self.tail.piece

            pieceSelected = [piece.left, piece.right]

            #verifica na peça enviada pelo jogador corresponde ao numero da peça do head
            if firstPiece.left in pieceSelected:
              #se a peça estiver ja na posição ele ja vai inserir
              if firstPiece.left == piece.right:
                pieceTemp.next = self.head
                self.head = pieceTemp
                # self.tail = pieceTemp
              else:
                  # se a peça n tiver na posicao correta ele inverte ele para quando for inserir fica lado com lado corretamente
                  pieceTemp.piece.invert()
                  pieceTemp.next = self.head
                  self.head = pieceTemp
                  # self.tail = pieceTemp
            elif lastPiece.right in pieceSelected:
              current = self.head
              while current.next:
                current = current.next
              current.next = pieceTemp
              self.tail = pieceTemp

              if lastPiece.right == piece.left:
                  current.next = pieceTemp
              else:
                  pieceTemp.piece.invert()
                  current.next = pieceTemp
            else:
                isAdded = False
                print('nao é possivel adicionar nada meu chapa')
                
        return isAdded
    # def size(self):
    #     atual = self.head
    #     contador = 0
    #     while atual != None:
    #         contador = contador + 1
    #         atual = atual.getNext()
    #     return contador

    # def search(self,item):
    #     atual = self.head
    #     encontrou = False
    #     while atual != None and not encontrou:
    #         if atual.getData() == item:
    #             encontrou = True
    #         else:
    #             atual = atual.getNext()
    #     return encontrou

    # def remove(self,item):
    #     atual = self.head
    #     anterior = None
    #     encontrou = False

    #     while not encontrou:
    #         if atual.getData() == item:
    #          encontrou = True
    #         else:
    #             anterior = atual
    #             atual = atual.getNext()

    #     if anterior == None:
    #         self.head = atual.getNext()
    #     else:
    #         anterior.setNext(atual.getNext())
