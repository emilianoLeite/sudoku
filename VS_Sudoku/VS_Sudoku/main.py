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
    print ("Iniciando geracao do sudoku")
    table = createTable()
    print (printMatrix(table))
    
    game = createGame(table,"easy")
    print("Easy:")
    print(printMatrix(game))
    print("Solving easy game...")
    print (printMatrix(solveGame(game)))   
    print("Solved.\n")
    
    game = createGame(table,"medium")
    print("Medium:")
    print(printMatrix(game))
    print("Solving medium game...")
    print (printMatrix(solveGame(game)))   
    print("Solved.\n")
    
    game = createGame(table,"hard")
    print("Hard:")
    print(printMatrix(game))
    print("Solving hard game...")
    print (printMatrix(solveGame(game)))   
    print("Solved.\n")