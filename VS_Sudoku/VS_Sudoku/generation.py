#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import copy

squares = {}#armazena todas as coordenadas para cada quadrado
squares[0] = [(0,0),(0,1),(0,2),
              (1,0),(1,1),(1,2),
              (2,0),(2,1),(2,2)]

squares[1] = [(0,3),(0,4),(0,5),
              (1,3),(1,4),(1,5),
              (2,3),(2,4),(2,5)]
          
squares[2] = [(0,6),(0,7),(0,8),
              (1,6),(1,7),(1,8),
              (2,6),(2,7),(2,8)]
          
squares[3] = [(3,0),(3,1),(3,2),
              (4,0),(4,1),(4,2),
              (5,0),(5,1),(5,2)]
          
squares[4] = [(3,3),(3,4),(3,5),
              (4,3),(4,4),(4,5),
              (5,3),(5,4),(5,5)]
          
squares[5] = [(3,6),(3,7),(3,8),
              (4,6),(4,7),(4,8),
              (5,6),(5,7),(5,8)]
          
squares[6] = [(6,0),(6,1),(6,2),
              (7,0),(7,1),(7,2),
              (8,0),(8,1),(8,2)]
          
squares[7] = [(6,3),(6,4),(6,5),
              (7,3),(7,4),(7,5),
              (8,3),(8,4),(8,5)]
          
squares[8] = [(6,6),(6,7),(6,8),
              (7,6),(7,7),(7,8),
              (8,6),(8,7),(8,8)]


def createTable():
    '''
    Cria matriz completa.
    '''
    currentMatrix = []
    while True:
        currentMatrix = generateInitMatrix()
        currentMatrix = [list(i) for i in zip(*currentMatrix)] #transposi��o da matriz
        random.shuffle(currentMatrix)
        if (random.random() <= 0,5):
            currentMatrix = [list(i) for i in zip(*currentMatrix)] #transposi��o da matriz
        if verifySquares(currentMatrix):
            break
    return currentMatrix

def getSquare(matrix,index):
    '''Retorna os n�meros do quadrado
    de �ndice 'index'.
    '''
    square = []
    for x,y in squares[index]:
            square.append(matrix[x][y])
    return square

def getSquareCoord(coord): 
    '''
    Retorna o par chave-valor do
    dicion�rio 'squares' que cont�m a coordenada
    'coord'.
    '''
    for i in squares:
        if coord in squares[i]:
            return squares[i]

def verifySquares(matrix):
    '''
    Verifica se h�
    incongru�ncias nos quadrados da
    matriz 'matrix'.
    '''
    for i in range(9):
        currentSquare = getSquare(matrix,i)
        if verifySquare(currentSquare) == False:
            return False #h� incongru�ncias
    return True

def verifySquare(square):
    '''
    Verifica se h�
    incongru�ncias no quadrado 'square'.
    '''
    for i in range(9):
        numOfOcurrences = square.count(square[i])
        if numOfOcurrences > 1:
            return False #h� incongru�ncias
    return True

def generateInitMatrix():
    '''
    Gera a matriz inicial, sorteando
    a ordem das linhas providas pela
    fun��o getInitRow.
    '''
    sorteador = [1,2,3,4,5,6,7,8,9]
    random.shuffle(sorteador)
    matrix = []
    for i in range(0,9):
            matrix.append( getInitRow(sorteador[i]) )
    return matrix

def getInitRow(index):
    row = {}
    row[1] = [1,2,3,4,5,6,7,8,9]
    row[2] = [2,3,4,5,6,7,8,9,1]
    row[3] = [3,4,5,6,7,8,9,1,2]
    row[4] = [4,5,6,7,8,9,1,2,3]
    row[5] = [5,6,7,8,9,1,2,3,4]
    row[6] = [6,7,8,9,1,2,3,4,5]
    row[7] = [7,8,9,1,2,3,4,5,6]
    row[8] = [8,9,1,2,3,4,5,6,7]
    row[9] = [9,1,2,3,4,5,6,7,8]
    return row[index]

def createGame(matrix, difficulty):
    '''
    Remove uma quantidade(estipulada pelo
    argumento 'difficulty') de n�meros da matriz
    'matrix', afim de gerar uma matriz "jog�vel".
    '''
    aux_matrix = copy.deepcopy(matrix)
    if (difficulty=='easy'):
        NUM = 30
    elif(difficulty=='medium'):
        NUM = 36
    elif(difficulty=='hard'):
        NUM = 40
    else:
        return NULL
 
    for qtd in range(NUM):
        x = random.randint(0,8)
        y = random.randint(0,8)       
        #Para nao repetir o local ja sorteado
        while aux_matrix[x][y] == 0:
            x = random.randint(0,8)
            y = random.randint(0,8) 
        aux_matrix[x][y] = 0
        game = aux_matrix
    return aux_matrix

def checkColumn(matrix, column, number):
    '''
    Verifica se existe uma ocorr�ncia
    de 'number' em 'column' dentro de 'matrix'.
    '''
    for row in matrix:
        if row[column] == number:
            return False #ja existe numero na coluna
    return True

def checkRow(matrix, row, number):
    '''
    Verifica se existe uma ocorr�ncia
    de 'number' em 'row' dentro de 'matrix'.
    '''
    for column in range(0,9):
        if matrix[row][column] == number:
            return False #ja existe numero na linha
    return True

def checkSquare(matrix,row,column,number):
    '''
    Verifica se existe uma ocorr�ncia
    de 'number' no quadrado que possui
    a coordenada ('row','column').
    '''
    coord = [row,column]
    for i in range(0,9): #varre as chaves do dicionario
        if coord in squares[i]:
            for x,y in squares[i]: #varre as coordenadas do quadrado
                if(matrix[x][y] == number):
                    return False #o numero ja existe no quadrado
            
    return True #o numero nao existe no quadrado

def isInsertable(game, row, column, number):
    '''
    Verifica se � poss�vel inserir 'number'
    na coordenada ('row','column') dentro de
    'game'.
    '''
    if( not checkRow(game, row, number) ):
        return False
    if( not checkColumn(game, column, number) ):
        return False
    if( not checkSquare(game, row, column, number) ):
        return False
    return True

def getSquaresDic():
    return squares