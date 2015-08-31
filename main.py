import random
import copy

squares = {} #armazena todas as coordenadas para cada quadrado
squares[1] = [[0,0],[0,1],[0,2],
              [1,0],[1,1],[1,2],
              [2,0],[2,1],[2,2]]

squares[2] = [[0,3],[0,4],[0,5],
              [1,3],[1,4],[1,5],
              [2,3],[2,4],[2,5]]

squares[3] = [[0,6],[0,7],[0,8],
              [1,6],[1,7],[1,8],
              [2,6],[2,7],[2,8]]

squares[4] = [[3,0],[3,1],[3,2],
              [4,0],[4,1],[4,2],
              [5,0],[5,1],[5,2]]

squares[5] = [[3,3],[3,4],[3,5],
              [4,3],[4,4],[4,5],
              [5,3],[5,4],[5,5]]

squares[6] = [[3,6],[3,7],[3,8],
              [4,6],[4,7],[4,8],
              [5,6],[5,7],[5,8]]

squares[7] = [[6,0],[6,1],[6,2],
              [7,0],[7,1],[7,2],
              [8,0],[8,1],[8,2]]

squares[8] = [[6,3],[6,4],[6,5],
              [7,3],[7,4],[7,5],
              [8,3],[8,4],[8,5]]

squares[9] = [[6,6],[6,7],[6,8],
              [7,6],[7,7],[7,8],
              [8,6],[8,7],[8,8]]

def createTable():
    currentMatrix = generateInitMatrix()
    currentMatrix = [list(i) for i in zip(*currentMatrix)]
    random.shuffle(currentMatrix)
    
    while ( not(verifySquares(currentMatrix) ) ):
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
    if index == 0:
        return [matrix[0][0],matrix[0][1],matrix[0][2],matrix[1][0],matrix[1][1],matrix[1][2],matrix[2][0],matrix[2][1],matrix[2][2]]
    if index == 1:
        return [matrix[0][3],matrix[0][4],matrix[0][5],matrix[1][3],matrix[1][4],matrix[1][5],matrix[2][3],matrix[2][4],matrix[2][5]]
    if index == 2:
        return [matrix[0][6],matrix[0][7],matrix[0][8],matrix[1][6],matrix[1][7],matrix[1][8],matrix[2][6],matrix[2][7],matrix[2][8]]
    if index == 3:
        return [matrix[3][0],matrix[3][1],matrix[3][2],matrix[4][0],matrix[4][1],matrix[4][2],matrix[5][0],matrix[5][1],matrix[5][2]]
    if index == 4:
        return [matrix[3][3],matrix[3][4],matrix[3][5],matrix[4][3],matrix[4][4],matrix[4][5],matrix[5][3],matrix[5][4],matrix[5][5]]
    if index == 5:
        return [matrix[3][6],matrix[3][7],matrix[3][8],matrix[4][6],matrix[4][7],matrix[4][8],matrix[5][6],matrix[5][7],matrix[5][8]]
    if index == 6:
        return [matrix[6][0],matrix[6][1],matrix[6][2],matrix[7][0],matrix[7][1],matrix[7][2],matrix[8][0],matrix[8][1],matrix[8][2]]
    if index == 7:
        return [matrix[6][3],matrix[6][4],matrix[6][5],matrix[7][3],matrix[7][4],matrix[7][5],matrix[8][3],matrix[8][4],matrix[8][5]]
    if index == 8:
        return [matrix[6][6],matrix[6][7],matrix[6][8],matrix[7][6],matrix[7][7],matrix[7][8],matrix[8][6],matrix[8][7],matrix[8][8]]
        
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
    for x in range(1,10): #varre as chaves do dicionário
        if square in squares[x]:
            for coordinate in squares[x]: #varre as coordenadas do quadrado
                if(matrix[coordinate[0]][coordinate[1]] == number):
                    return False #o número já existe no quadrado
            
    return True #o número não existe no quadrado

def verifySquares(matrix):
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
        #print("ROW")
        return False
    if( not checkColumn(matrix, column, number) ):
        #print("column")
        return False
    if( not checkSquare(matrix, row, column, number) ):
        #print("square")
        return False
    return True

def basicCheck(game,coordinate):
    insertNumber = 0
    insertableNumbers = 0
    for number in range(1,10):
        if (isInsertable(game, coordinate[0], coordinate[1], number)):
            insertNumber = number
            insertableNumbers+=1
    if (insertableNumbers == 1):
        game[coordinate[0]][coordinate[1]] = insertNumber
        return True
    return False
               
def solveGame(game):
    coordinates = getCoordinates(game,0)
    print(coordinates)
    while(coordinates): #while coordinates is not empty        
        for coordinate in coordinates:
            if(basicCheck(game,coordinate)):
                coordinates.remove(coordinate)
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
    print (printMatrix(solveGame(game)))
