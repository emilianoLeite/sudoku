import random
import copy

def createTable():
    currentMatrix = generate_init_matrix()
    currentMatrix = [list(i) for i in zip(*currentMatrix)]
    random.shuffle(currentMatrix)
    #while verifyColumns(currentMatrix) == False:
    #    print(".")
    #currentMatrix = generate_init_matrix()

    
    
    while verifySquares(currentMatrix) == False:
        currentMatrix = generate_init_matrix()
        currentMatrix = [list(i) for i in zip(*currentMatrix)]
        random.shuffle(currentMatrix)
   
    return currentMatrix

#def generate_rand_matrix():
#    matrix = [generate_rand_row(),generate_rand_row(),generate_rand_row(),generate_rand_row(),generate_rand_row(),generate_rand_row(),generate_rand_row(),generate_rand_row(),generate_rand_row()]
#    return matrix

def generate_init_matrix():
    sorteador = [1,2,3,4,5,6,7,8,9]

    random.shuffle(sorteador)
    
    matrix = [get_init_row(sorteador[0]),get_init_row(sorteador[1]),get_init_row(sorteador[2]),
              get_init_row(sorteador[3]),get_init_row(sorteador[4]),get_init_row(sorteador[5]),
              get_init_row(sorteador[6]),get_init_row(sorteador[7]),get_init_row(sorteador[8])]

    return matrix

def get_init_row(index):
    testeArray = [1,2,3,4,5,6,7,8,9]
    testeArray2 = [2,3,4,5,6,7,8,9,1]
    testeArray3 = [3,4,5,6,7,8,9,1,2]
    testeArray4 = [4,5,6,7,8,9,1,2,3]
    testeArray5 = [5,6,7,8,9,1,2,3,4]
    testeArray6 = [6,7,8,9,1,2,3,4,5]
    testeArray7 = [7,8,9,1,2,3,4,5,6]
    testeArray8 = [8,9,1,2,3,4,5,6,7]
    testeArray9 = [9,1,2,3,4,5,6,7,8]
    if index == 1:
        return testeArray
    if index == 2:
        return testeArray2
    if index == 3:
       return testeArray3
    if index == 4:
        return testeArray4
    if index == 5:
        return testeArray5
    if index == 6:
        return testeArray6
    if index == 7:
        return testeArray7
    if index == 8:
        return testeArray8
    if index == 9:
        return testeArray9

def print_matrix(matrix):
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


def setColumn(matrix,index):
    #TODO
    return

def getColumn(matrix,index):
    return [row[index] for row in matrix]

#def verifyColumns(matrix):
#    for i in range(9):
#        currentColumn = getColumn(matrix,i)
#        print (print_row(currentColumn))
#        if verifyColumn(currentColumn) == False:
#            return False
#    return True

#def verifyColumn(column):
#    for i in range(9):
#        numOfOcurrences = column.count(column[i])
#        if numOfOcurrences > 1:
#            return False
#   return True

def checkColumn(matrix, column, number):
    for row in matrix:
        if row[column] == number:
            return False #number already in column
    return True

def checkRow(matrix, row, number):
    for column in range(0,9):
        if matrix[row][column] == number:
            return False #number already in row
    return True

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

#def generate_rand_row():
#    row = [1,2,3,4,5,6,7,8,9]
#    random.shuffle(row)
#    return row

def print_row(row):
    result = ""
    for r in row:
        result = result + str(r) + " "
    return result

def createGame(matrix, difficulty):
    aux_matrix = copy.deepcopy(matrix)
    if (difficulty=='easy'):
        NUM = 18
    else:
        return NULL
    """elif(difficulty=='medium'):
        NUM = 22
    elif(difficulty=='hard'):
        NUM = 26"""


    for qtd in range(0,NUM):
        x = random.randint(0,8)
        y = random.randint(0,8)
        """while(not [x,y] in aux_matrix[qtd]):
            x = random.randint(0,8)
            y = random.randint(0,8)
            print('.')"""
        #aux_matrix.remove([x,y])
        aux_matrix[x][y] = 0
    return aux_matrix
    
if __name__ == '__main__':
    print ("Iniciando geração do sudoku")
    table = createTable()
    print (print_matrix(table))
    game = createGame(table,"easy")
    print(print_matrix(game))
    
