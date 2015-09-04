from generation import *
from solution import *

def printMatrix(matrix):
    result = ""
    for i in range(9):
        result += "\n" if i%3==0 else ""
        for j in range(9):
            result += " " if (not j==0 and j%3==0) else ""
            result = result + str(matrix[i][j]) + " "
        result = result + "\r\n"
    return result

if __name__ == '__main__':
    print ("Iniciando geracao do sudoku")
    table = createTable()
    print (printMatrix(table))
    
    game = createGame(table,"easy")
    print("Easy:")
    print(printMatrix(game))
    
    game = createGame(table,"medium")
    print("Medium:")
    print(printMatrix(game))
    
    game = createGame(table,"hard")
    print("Hard:")
    print(printMatrix(game))
