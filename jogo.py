import os
from utils import *
from player import Player
from typing import List
from lista import ListHandsPieces
from domino import ListPieces

class Jogo:
    def __init__(self):
        self.ganhador: Player = None
        self.pecas = []
        self.jogadores: List[Player] = []

    def start(self):
        os.system('cls')
        print('Iniciando o jogo...')
        sleep(2)
        os.system('cls')

        self.addPlayers()
        self.getPieces()
        self.sendPiecesForPlayers()

        domino = ListPieces()

        empate = False
        contaPular = 0

        while self.ganhador == None and not empate:
            for jogador in self.jogadores:
                isPlayed = False
                isWin = False


                while not isPlayed and not isWin:
                    
                    print(f'Jogo: {domino if domino.head != None else "Mesa vazia"}')

                    print(f'\nJogador da vez: {jogador.name}')
                    print('________________________')
                    jogador.showMyHands()
                    print('________________________')

                    opcao = int(input('\nDigite a opção da peça desejada: '))

                    if opcao != 0:
                        piece = jogador.searchPiece(opcao)

                        if piece != None:
                            isAdded = domino.add(piece)
                            
                            if isAdded:
                                os.system("cls")
                                contaPular = 0
                                isPlayed = True
                                jogador.removePiece(opcao)
                                if jogador.getQtdPieces() ==0:
                                    isWin= True
                                    self.ganhador = jogador
                                    break
                    else:
                        contaPular+=1

                        if contaPular == len(self.jogadores):
                            empate = True
                            
                            break

                    
                        isPlayed = True
        if self.ganhador:
            print(f'Ganhador {self.ganhador.name}')
        else:
            ganhadorTemp: Player = None
            points = 0
            empate = False

            for jogador in self.jogadores:
                if ganhadorTemp == None:
                    ganhadorTemp = jogador
                    points += jogador.countPoints()
                else:
                    nextJogadorPoints = jogador.countPoints()
                    if points > nextJogadorPoints:
                        ganhadorTemp = jogador
                        points = nextJogadorPoints
                    elif points == nextJogadorPoints:
                        empate = True
                    else:
                        empate = False
            print(f'Ganhador {ganhadorTemp.name} com total de {points} pontos' if empate == False else f'Houve empate senhores')

    def addPlayers(self):
        codition = False

        while not codition:
            quantity = int(input('Digite a quantidade de Jogadores: '))
            if quantity > 1 and quantity<=4:
                for i in range(quantity):
                    name = input(f'Digite o nome do {i+1}° Jogador: ')
                    player = Player(name)
                    self.jogadores.append(player)
                codition= True
            else:
                print('É preciso no minimo 2 jogadores e no máximo 4.')
            os.system('cls')

    def getPieces(self):
        self.pecas = sortPieces(generatePieces())

    def sendPiecesForPlayers(self):
        for jogador in self.jogadores:
            piecesSelected = ListHandsPieces()
            for i in range(7):
                peca = self.pecas.pop()
                piecesSelected.add(peca)
            jogador.getPecas(piecesSelected)
