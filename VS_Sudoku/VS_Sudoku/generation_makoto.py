#-*- coding: utf-8 -*-
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
    while True:
        currentMatrix = generateInitMatrix()
        if (random.random() <= 0.5):
            #fazer shuffle apenas de tres em tres linhas
            aux = currentMatrix[:3]
            random.shuffle(aux)
            currentMatrix[:3] = aux
            
            aux = currentMatrix[3:6]
            random.shuffle(aux)
            currentMatrix[3:6] = aux
            
            aux = currentMatrix[6:]
            random.shuffle(aux)
            currentMatrix[6:] = aux
            
        if (random.random() <= 0.5):
            currentMatrix = [list(i) for i in zip(*currentMatrix)] #transposição da matriz
        if verifySquares(currentMatrix):
            break
    return currentMatrix

def generateInitMatrix():
    '''
    Gera a matriz inicial, sorteando
    um número para cada letra(A..I)
    e inserindo-os numa ordem que é
    conhecidamente correta.

    Créditos a Edison Makoto.
    '''
    sorteador = [1,2,3,4,5,6,7,8,9]
    random.shuffle(sorteador)
    A = sorteador[0]
    B = sorteador[1]
    C = sorteador[2]
    D = sorteador[3]
    E = sorteador[4]
    F = sorteador[5]
    G = sorteador[6]
    H = sorteador[7]
    I = sorteador[8]
    sudoku= [
                [A,B,C, D,E,F, G,H,I],
                [D,E,F, G,H,I, A,B,C],
                [G,H,I, A,B,C, D,E,F],
                [B,C,A, E,F,D, H,I,G],
                [E,F,D, H,I,G, B,C,A],
                [H,I,G, B,C,A, E,F,D],
                [C,A,B, F,D,E, I,G,H],
                [F,D,E, I,G,H, C,A,B],
                [I,G,H, C,A,B, F,D,E],
            ]
    return sudoku

def verifySquares(matrix):
    '''
    Verifica se há
    incongruências nos quadrados da
    matriz 'matrix'.
    '''
    for i in range(9):
        currentSquare = getSquare(matrix,i)
        if verifySquare(currentSquare) == False:
            return False #há incongruências
    return True

def verifySquare(square):
    '''
    Verifica se há
    incongruências no quadrado 'square'.
    '''
    for i in range(9):
        numOfOcurrences = square.count(square[i])
        if numOfOcurrences > 1:
            return False #há incongruências
    return True

def getSquare(matrix,index):
    '''Retorna os números do quadrado
    de índice 'index'.
    '''
    square = []
    for x,y in squares[index]:
            square.append(matrix[x][y])
    return square

def getSquareCoord(coord): 
    '''
    Retorna o par chave-valor do
    dicionário 'squares' que contém a coordenada
    'coord'.
    '''
    for i in squares:
        if coord in squares[i]:
            return squares[i]

def createGame(matrix, difficulty):
    '''
    Remove uma quantidade(estipulada pelo
    argumento 'difficulty') de números da matriz
    'matrix', afim de gerar uma matriz "jogável".
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
    Verifica se existe uma ocorrência
    de 'number' em 'column' dentro de 'matrix'.
    '''
    for row in matrix:
        if row[column] == number:
            return False #ja existe numero na coluna
    return True

def checkRow(matrix, row, number):
    '''
    Verifica se existe uma ocorrência
    de 'number' em 'row' dentro de 'matrix'.
    '''
    for column in range(0,9):
        if matrix[row][column] == number:
            return False #ja existe numero na linha
    return True

def checkSquare(matrix,row,column,number):
    '''
    Verifica se existe uma ocorrência
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
    Verifica se é possível inserir 'number'
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
