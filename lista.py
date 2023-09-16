from domino import Piece, PieceNode

class  ListHandsPieces:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.head)

    def is_empty(self):
        return self.head == None

    def add(self,piece:Piece):
        temp = PieceNode(piece)
        temp.next = self.head
        self.head = temp

    def size(self):
        atual = self.head
        contador = 0
        while atual != None:
            contador = contador + 1
            atual = atual.getNext()
        return contador

    def search(self,item):
        atual = self.head
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                atual = atual.getNext()
        return encontrou

    def remove(self,item):
        atual = self.head
        anterior = None
        encontrou = False

        while not encontrou:
            if atual.getData() == item:
             encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()

        if anterior == None:
            self.head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())
