from generation import *
from solution import *

def printMatrix(matrix):
    result = ""
    for i in range(9):
        for j in range(9):
            result = result + str(matrix[i][j]) + " "
        result = result + "\r\n"
    return result

def getRow(matrix,index):
    return matrix[:][index]

def getColumn(matrix,index):
    return [row[index] for row in matrix]


def printRow(row):
    result = ""
    for r in row:
        result = result + str(r) + " "
    return result

if __name__ == '__main__':
    """print ("Iniciando geração do sudoku")
    table = createTable()
    print (printMatrix(table))
    game = createGame(table,"easy")"""
    game  =[
            [0, 0, 8, 6, 5, 4, 0, 9, 2], 
            [0, 0, 0, 0, 8, 7, 4, 0, 5], 
            [5, 4, 6, 9, 2, 1, 7, 6, 8], 
            [9, 8, 0, 5, 7, 6, 3, 2, 4], 
            [6, 5, 7, 2, 4, 3, 9, 8, 1], 
            [0, 2, 4, 8, 1, 9, 6, 5, 7], 
            [8, 9, 2, 4, 6, 5, 0, 1, 3], 
            [7, 6, 0, 0, 9, 8, 5, 4, 0], 
            [0, 0, 0, 1, 3, 2, 8, 7, 9]
           ]
    #game = createGame(table,"medium")
    #game = createGame(table,"hard")
    print(printMatrix(game))
    print("Solving game...")
    #possibilities[0,0] = [8,9]
    #possibilities[0,1] = [4]
    #print(possibilities)
    #duo = possibilities[0,0] if (len(possibilities[0,0]) == 2) else []
    
    print (printMatrix(solveGame(game)))   
    print("Solved.")
