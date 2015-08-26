import random
#print(random.randint(1, 9))

sudoku = []
def insert(row,column,number):
    for linha in range(0,9):
        if(linha==row):
            for coluna in range(0,9):
                if(sudoku[linha][coluna]==number):#verifica as colunas
                    return False
        if(sudoku[linha][column]==number):
            return False

    sudoku[row][column] = number
    return True
    
if __name__ == '__main__':
    
    for x in range(0, 9):
        sudoku.append([])
        for y in range(0, 9):
            sudoku[x].append(0)

    row=0
    column=0
    while(True):
        x=random.randint(1, 9)
        if(insert(row,column,x)):
            print(x)
            column+=1
            if(column==9):
                for abc in sudoku:
                    for dhf in abc:
                        print(dhf),
                    print("\n")
                row+=1
                column=0
                
            if(row==9):
                break
                
    for row in sudoku:
        for column in row:
            print(column),
        print("\n")
