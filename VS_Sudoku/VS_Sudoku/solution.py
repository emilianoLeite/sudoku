#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generation import isInsertable, getSquaresDic, getSquareCoord

squares = getSquaresDic()
possibilities = {} #armazena todas as possibilidades de cada coordenada

def solveGame(game):
    while True: 
        coordinates = getCoordinates(game,0) #coordenadas a serem preenchidas
        #print(coordinates)
        if not coordinates:
            break

        possibilities.clear()
        for row,column in coordinates: 
            populatePossibilities(game,row,column)
        
        #basicPopulate(game)
        pairPopulate(game)

        #break
        #loop infinito se itens com mais de uma possibilidade
    return game


def getCoordinates(matrix,number):
    '''
    Return an array of coordinates 
    inside array 'matrix' where 'number' is present
    '''
    coordinates =[]
    for x in range(0,9):
        for y in range(0,9):
            if matrix[x][y] == number:
                coordinates.append( [x,y] )
    return coordinates

def populatePossibilities(game,row,column):
    '''
    Popula o dicionário 'possibilities'
    com todas as possibilidades para uma
    dada coordenada('row','column') dentro da
    matrix 'game'
    '''
    for number in range(1,10):
        #Verifica row, column and square
        if (isInsertable(game, row, column, number)):
            #print("Row ",row," Column ", column," N ",number)
            if (row,column) in possibilities: 
                possibilities[(row,column)].append(number)
            else:
                possibilities[(row,column)] = [number]
            #print(possibilities)

def basicPopulate(game):
    '''
    Popula o jogo nas coordenadas
    onde apenas um número e possível
    '''
    for key in possibilities:
        if len(possibilities[key]) == 1:
            game[key[0]][key[1]] = possibilities[key][0]
            
def pairPopulate(game):
    '''
    Reduz o espectro de possibilidades baseado
    na verificação de pares:
    Se um quadrado possui mais de uma coordenada 
    onde apenas 2 números são possíveis, então pode-se
    remover das outras coordenadas a possibilidade desses
    dois números.
    '''
    duoKeys = []
    alreadyChecked = []
    for key in possibilities:
        if not key in alreadyChecked:
            #apenas dois possibilidades para a coordenada
            if (len(possibilities[key]) == 2):
                duo = possibilities[key] #os dois valores possiveis
                square = getSquareCoord(key) #array com todas as coordenadas do quadrado onde duo se encontra
                moreDuos = hasMultiplePairs(square,duo)#array com as coordenadas onde o mesmo par de duo ocorre(incluindo a ocorrencia original)
                if len(moreDuos) > 1: #existem outros pares identicos, alem do original
                    for coord in moreDuos:
                        alreadyChecked.append(coord)
                    for coord in square: #varre todas as coordenadas do quadardo
                        if  coord in possibilities and not coord in moreDuos: #verifica todos as outras coordenadas do quadrado
                            if duo[0] in possibilities[coord]:
                                possibilities[coord].remove(duo[0]) 
                            if duo[1] in possibilities[coord]:
                                possibilities[coord].remove(duo[1])     
    basicPopulate(game)

def hasMultiplePairs(square,duo):
    '''
    Verifica se um quadrado 'square'
    possui mais de uma coordenada onde as
    únicas possibilidades são os números 
    contidos em 'duo'
    '''
    pairs =[]
    for coordinate in square:
        if coordinate in possibilities and possibilities[coordinate] == duo:
            pairs.append(coordinate)
    return pairs