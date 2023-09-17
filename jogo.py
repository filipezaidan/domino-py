import os
from utils import *
from player import Player
from typing import List
from lista import ListHandsPieces
from domino import ListPieces



class Jogo:
    def __init__(self): # Construtor
        self.playerWin: Player = None
        self.pieces = []
        self.players: List[Player] = []

    def start(self): # Inicia o jogo
        loading('Iniciando o jogo')

        self.addPlayers()
        self.getPieces()
        self.sendPiecesForPlayers()

        domino = ListPieces() # Cria a lista encadeada das peças do jogo

        isTie = False
        countTurn = 0

        while self.playerWin == None and not isTie: # Enquanto não houver ganhador e não der empate
            for player in self.players: # Turnos
                isPlayed = False
                hasWon = False


                while not isPlayed and not hasWon: # Enquanto não tiver jogado e não tiver ganho
                    
                    print(f'Jogo: {domino if domino.head != None else "Mesa vazia"}')

                    print(f'\nJogador da vez: {player.name}')
                    
                    print('________________________')
                    player.showPieces() # Mostra as peças do jogador
                    print('________________________')

                    option = int(input('\nEscolha uma opção de peça para jogar: ')) # Escolhe uma opção de pega pra jogar

                    if option != 0: # Joga a peça
                        piece = player.searchPiece(option) # Pega a peça selecionada

                        if piece != None:
                            isAdded = domino.add(piece) # Adiciona a peça no jogo
                            
                            if isAdded: # Caso tenha sido possível adicionar
                                cls()
                                countTurn = 0
                                isPlayed = True
                                player.removePiece(option)

                                if player.sizePieces() == 0:
                                    hasWon = True
                                    self.playerWin = player
                                    break
                    else: # Passa a vez
                        countTurn+=1

                        if countTurn == len(self.players):
                            isTie = True
                            break

                        isPlayed = True

                # Para o jogo assim que estiver um ganhador ou empate
                # if self.playerWin is not None or isTie is not False:
                if self.playerWin or isTie:
                    break

        # Após o jogo acabar

        if self.playerWin: # Se alguém bateu, mostra quem ganhou
            print(f'Ganhador: {self.playerWin.name}, parabéns {self.playerWin.name}!')

        else: # Caso ninguém tenha batido, vai pra contagem de pontos
            tempWinner: Player = None # Ganhador temporário
            tempWinnerPoints = 0 # Pontuação do ganhador temporário

            isTie = False # Diz se deu empate ou não

            for player in self.players: # Para cada jogador
                
                if tempWinner == None: # No primeiro jogador, define-o como temporário e calcula seus pontos
                    tempWinner = player 
                    tempWinnerPoints += player.countPoints()

                else: # Do segundo jogador em diante, pega seus pontos, compara com os pontos do jogador anterior e define ou não um novo ganhador temporário
                    currentPlayerPoints = player.countPoints() # Pega a pontuação do jogador atual

                    # Compara a pontuação do jogador atual com a pontuação do ganhador temporário
                    if tempWinnerPoints > currentPlayerPoints: # Se a pontuação do jogador atual for maior, atualiza o ganhador temporário e a pontuação dele
                        tempWinner = player
                        tempWinnerPoints = currentPlayerPoints

                    elif tempWinnerPoints == currentPlayerPoints: # Se a ponturação do jogador atual for igual a pontuação do ganhador temporário, dá empate
                        isTie = True
                        break

            print(f'Ganhador: {tempWinner.name}, com total de {tempWinnerPoints} pontos!' if isTie == False else f'Houve empate, senhores!')

    def addPlayers(self): # Adiciona os jogadores
        condition = False

        while not condition:
            quantity = int(input('Digite a quantidade de Jogadores: '))

            if quantity > 1 and quantity<=4:
                for i in range(quantity): # Para cada jogador pergunta o nome
                    name = input(f'Digite o nome do {i+1}° Jogador: ')
                    player = Player(name)
                    self.players.append(player)

                condition= True

            else: # Mínimo de 2 jogadores e 4 no máximo
                print('É preciso no minimo 2 jogadores e no máximo 4.')

            cls()

    def getPieces(self): # Gera as peças e embralha elas
        self.pieces = sortPieces(generatePieces())

    def sendPiecesForPlayers(self): # Distruibui a mão de cada jogador
        for jogador in self.players:  
            piecesSelected = ListHandsPieces() # Cria a lista encadeada da mão do jogador
            for i in range(7):
                peca = self.pieces.pop() # Remove a peça da lista de peças
                piecesSelected.add(peca) # Adiciona a peça na mão do jogador
            jogador.addPieces(piecesSelected) # Adiciona a mão do jogador
