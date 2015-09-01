import random
import copy

squares = {} #armazena todas as coordenadas para cada quadrado
squares[0] = [[0,0],[0,1],[0,2],
              [1,0],[1,1],[1,2],
              [2,0],[2,1],[2,2]]

squares[1] = [[0,3],[0,4],[0,5],
              [1,3],[1,4],[1,5],
              [2,3],[2,4],[2,5]]

squares[2] = [[0,6],[0,7],[0,8],
              [1,6],[1,7],[1,8],
              [2,6],[2,7],[2,8]]

squares[3] = [[3,0],[3,1],[3,2],
              [4,0],[4,1],[4,2],
              [5,0],[5,1],[5,2]]

squares[4] = [[3,3],[3,4],[3,5],
              [4,3],[4,4],[4,5],
              [5,3],[5,4],[5,5]]

squares[5] = [[3,6],[3,7],[3,8],
              [4,6],[4,7],[4,8],
              [5,6],[5,7],[5,8]]

squares[6] = [[6,0],[6,1],[6,2],
              [7,0],[7,1],[7,2],
              [8,0],[8,1],[8,2]]

squares[7] = [[6,3],[6,4],[6,5],
              [7,3],[7,4],[7,5],
              [8,3],[8,4],[8,5]]

squares[8] = [[6,6],[6,7],[6,8],
              [7,6],[7,7],[7,8],
              [8,6],[8,7],[8,8]]

def createTable():
    currentMatrix = []
    while ( not verifySquares(currentMatrix) ):
        currentMatrix = generateInitMatrix()
        #transpõe matriz
        currentMatrix = [list(i) for i in zip(*currentMatrix)]
        random.shuffle(currentMatrix)
    return currentMatrix

def generateInitMatrix():
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

def printMatrix(matrix):
    result = ""
    for i in range(9):
        for j in range(9):
            result = result + str(matrix[i][j]) + " "
        result = result + "\r\n"
    return result

def getSquare(matrix,index):
    square = []
    for x,y in squares[index]:
            square.append(matrix[x][y])
    return square

def getRow(matrix,index):
    return matrix[:][index]

def getColumn(matrix,index):
    return [row[index] for row in matrix]

def checkColumn(matrix, column, number):
    for row in matrix:
        if row[column] == number:
            return False #já existe número na already na coluna
    return True

def checkRow(matrix, row, number):
    for column in range(0,9):
        if matrix[row][column] == number:
            return False #já existe número na linha
    return True

def checkSquare(matrix,row,column,number):
    square = [row,column]
    for i in range(0,9): #varre as chaves do dicionário
        if square in squares[i]:
            for x,y in squares[i]: #varre as coordenadas do quadrado
                if(matrix[x][y] == number):
                    return False #o número já existe no quadrado
            
    return True #o número não existe no quadrado

def verifySquares(matrix):
    if not matrix:
        return False
    for i in range(9):
        currentSquare = getSquare(matrix,i)
        if verifySquare(currentSquare) == False:
            return False
    return True

def verifySquare(square):
    for i in range(9):
        numOfOcurrences = square.count(square[i])
        if numOfOcurrences > 1:
            return False
    return True

def printRow(row):
    result = ""
    for r in row:
        result = result + str(r) + " "
    return result

def createGame(matrix, difficulty):
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
        #Para não repetir o local ja sorteado
        while aux_matrix[x][y] == 0:
            x = random.randint(0,8)
            y = random.randint(0,8) 
        aux_matrix[x][y] = 0
    return aux_matrix

def isInsertable(matrix, row, column, number):
    if( not checkRow(matrix, row, number) ):
        return False
    if( not checkColumn(matrix, column, number) ):
        return False
    if( not checkSquare(matrix, row, column, number) ):
        return False
    return True

def basicCheck(game,row,column):
    insertNumber = 0
    insertableNumbers = 0
    for number in range(1,10):
        if (isInsertable(game, row, column, number)):
            insertNumber = number
            insertableNumbers+=1
    if (insertableNumbers == 1):
        game[row][column] = insertNumber
        return True
    return False
               
def solveGame(game):
    coordinates = getCoordinates(game,0)
    #print(coordinates)
    while(coordinates): #while coordinates is not empty        
        for row,column in coordinates:
            if(basicCheck(game,row,column)):
                coordinates.remove([row,column])
                break                
    return game

#Get an array of coordinates equal to 'number' inside array 'matrix'
def getCoordinates(matrix,number):
    coordinates =[]
    for x in range(0,9):
        for y in range(0,9):
            if game[x][y] == 0:
                coordinates.append( [x,y] )
    return coordinates
 
if __name__ == '__main__':
    print ("Iniciando geração do sudoku")
    table = createTable()
    print (printMatrix(table))
    game = createGame(table,"hard")
    print(printMatrix(game))
    print("Solving game...")
    print (printMatrix(solveGame(game)))
