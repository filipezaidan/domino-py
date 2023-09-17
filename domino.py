class Piece:
  def __init__(self, left: int, right: int): # Construtor da classe das peças
    self.left = left
    self.right = right

  def __str__(self): # Print
    return f'[{self.left}|{self.right}]'

  def invert(self): # Inverte os lados das peças
      temp = self.left
      self.left = self.right
      self.right = temp
  
  def getPoints(self): # Soma os lados das peças para saber os pontos dela
      return self.left + self.right

class PieceNode: # Classe nó que armazenará uma peça
    def __init__(self, piece: Piece): # Construtor
        self.piece = piece
        self.next = None

    def __repr__(self): # Print
        if self.next is not None:
            return '[%s|%s]  %s' % (self.piece.left, self.piece.right, self.next)
        else:
            return '[%s|%s]' % (self.piece.left, self.piece.right)

    def getData(self): # Retorna a peça
        return self.piece
    
    def getNext(self): # Rertorna a próxima peça
        return self.next
    
    def setData(self, new_piece): # Atualiza o valor da peça
        self.piece = new_piece

    def setNext(self, new_next): # Atualiza o valor da próxima peça
        self.next = new_next

class  ListPieces: # Classe da lista de peças jogadas
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self): # Print
        return str(self.head)

    def is_empty(self): # Verifica se está vazia
        return self.head == None

    def add(self, piece: Piece): # Adiciona uma peça na lista de peças jogadas
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

              while current.next: # Encontra a última peça
                current = current.next

              current.next = pieceTemp
              self.tail = pieceTemp

              # Verifica de qual lado a peça será colocada
              if lastPiece.right == piece.left:
                  current.next = pieceTemp
              else:
                  pieceTemp.piece.invert()
                  current.next = pieceTemp
            else: # Caso a peça não possa ser adicionada
                isAdded = False
                print('\n Essa peça não pode ser adicionada (estou de olho) \n') # Comentário do Lucas: KKKKKKKK, olhando se é gato por lebre é
                
        return isAdded