import os
from utils import *
from player import Player
from typing import List
from lista import ListHandsPieces
from domino import ListPieces

class Jogo:
    def __init__(self):
        self.playerWin: Player = None
        self.pieces = []
        self.players: List[Player] = []

    def start(self):
        os.system('cls')
        print('Iniciando o jogo...')
        sleep(2)
        os.system('cls')

        self.addPlayers()
        self.getPieces()
        self.sendPiecesForPlayers()

        domino = ListPieces()

        isTie = False
        countTurn = 0

        while self.playerWin == None and not isTie:
            for player in self.players:
                isPlayed = False
                isWin = False


                while not isPlayed and not isWin:
                    
                    print(f'Jogo: {domino if domino.head != None else "Mesa vazia"}')

                    print(f'\nJogador da vez: {player.name}')
                    print('________________________')
                    player.showPieces()
                    print('________________________')

                    option = int(input('\nDigite a opção da peça desejada: '))

                    if option != 0:
                        piece = player.searchPiece(option)

                        if piece != None:
                            isAdded = domino.add(piece)
                            
                            if isAdded:
                                os.system("cls")
                                countTurn = 0
                                isPlayed = True
                                player.removePiece(option)
                                if player.sizePieces() ==0:
                                    isWin= True
                                    self.playerWin = player
                                    break
                    else:
                        countTurn+=1

                        if countTurn == len(self.players):
                            isTie = True
                            break
                        isPlayed = True
                #sai do for assim que estiver um ganhador ou empate
                if self.playerWin is not None or isTie is not False:
                    break
        if self.playerWin:
            print(f'Ganhador {self.playerWin.name}')
        else:
            ganhadorTemp: Player = None
            points = 0
            isTie = False

            for player in self.players:
                if ganhadorTemp == None:
                    ganhadorTemp = player
                    points += player.countPoints()
                else:
                    nextJogadorPoints = player.countPoints()
                    if points > nextJogadorPoints:
                        ganhadorTemp = player
                        points = nextJogadorPoints
                    elif points == nextJogadorPoints:
                        isTie = True
                    else:
                        isTie = False
            print(f'Ganhador {ganhadorTemp.name} com total de {points} pontos' if isTie == False else f'Houve empate senhores')

    def addPlayers(self):
        codition = False

        while not codition:
            quantity = int(input('Digite a quantidade de Jogadores: '))
            if quantity > 1 and quantity<=4:
                for i in range(quantity):
                    name = input(f'Digite o nome do {i+1}° Jogador: ')
                    player = Player(name)
                    self.players.append(player)
                codition= True
            else:
                print('É preciso no minimo 2 jogadores e no máximo 4.')
            os.system('cls')

    def getPieces(self):
        self.pieces = sortPieces(generatePieces())

    def sendPiecesForPlayers(self):
        for jogador in self.players:
            piecesSelected = ListHandsPieces()
            for i in range(7):
                peca = self.pieces.pop()
                piecesSelected.add(peca)
            jogador.addPieces(piecesSelected)
