import random

sudoku = []
squares = {}
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

def check_square(row,column,number):
    square = [row,column]
    

    for x in range(1,10): #varre as chaves do dicionário
        if square in squares[x]:
            for coordinate in squares[x]: #varre as coordenadas do quadrado
                if(sudoku[coordinate[0]][coordinate[1]] == number):
                    return False #o número já existe no quadrado
            
    return True #o número não existe no quadrado
        
def possible(row,column,number):
    #tentar modular em check_row, check_column e check_square
    if(not check_square(row,column,number)):
        return False
    for linha in range(0,9):
        if(linha==row):
            for coluna in range(0,9):
                if(sudoku[linha][coluna]==number):#verifica as colunas
                    return False
        if(sudoku[linha][column]==number):
            return False
        
    return True

def insert(row,column,number):
    if(possible(row,column,number)):
        sudoku[row][column] = number
        return True
    return False

def createTable(): #nao funciona se nao esta no main
    for x in range(0, 9):
        sudoku.append([])
        for y in range(0, 9):
            sudoku[x].append(0)

    #row=0
    #column=0

    for x in range(1,10): #varre as chaves do dicionário
        inserted=0
        while(True):
            for coordinate in squares[x]:
                row = coordinate[0]
                column = coordinate[1]
                while(True):
                    x=random.randint(1, 9)
                    if(insert(row,column,x)):
                        print("Row", row, end="")
                        print(" Column", column, end="")
                        print(" N",x)
                        inserted+=1
                        break
            if(inserted==9):
                for abc in sudoku:
                    for dhf in abc:
                        print(dhf, end="")
                    print("\n")
                break
                
    for row in sudoku:
        for column in row:
            print(column, end="")
        print("\n")
    
if __name__ == '__main__':
    createTable()
