from domino import Piece, PieceNode

# Classe da lista encadeada que servirá para construir a mão do jogo
class  ListHandsPieces:
    def __init__(self): # Construtor da classe de lista encadeada
        self.head = None # Variável que serve como o primeiro nó da lista

    def __repr__(self): # Print
        return str(self.head)

    def is_empty(self): # Verifica se a lista encadeada está vazia
        return self.head == None

    def add(self, piece: Piece): # Adiciona uma nova peça na lista encadeada
        temp = PieceNode(piece)
        temp.next = self.head
        self.head = temp

    def size(self): # Retorna o tamanho da lista encadeada
        atual = self.head
        contador = 0
        while atual != None:
            contador = contador + 1
            atual = atual.getNext()
        return contador

    def search(self, piece): # Busca uma peça específica na lista encadeada
        atual = self.head
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData() == piece:
                encontrou = True
            else:
                atual = atual.getNext()
        return encontrou

    def remove(self, piece): # Remomve uma peça da lista encadeada
        atual = self.head
        anterior = None
        encontrou = False

        while not encontrou: # Procura a peça
            if atual.getData() == piece:
             encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()

        if anterior == None:
            self.head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())
