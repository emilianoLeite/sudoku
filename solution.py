from generation import isInsertable

possibilities = {} #armazena todas as possibilidades de cada coordenada

def solveGame(game):
    
    """coordinates = getCoordinates(game,0)
    #print(coordinates)
    while(coordinates): #while coordinates is not empty        
        for row,column in coordinates:
            if(basicCheck(game,row,column)):
                coordinates.remove([row,column])
                break
            if duoCheck(game,row,column,possibilities):
                coordinates.remove([row,column])
                break
    return game"""
    
    while True: #loop infinito (versão python de um bloco do-while)
        coordinates = getCoordinates(game,0)
        print(coordinates) #é isso aqui que está printando eternamente
        if not coordinates:
            break
        #Para cada coordenada tenta resolução
        for row,column in coordinates:
            possibilities.clear()
            addPossibilitiesToDictionary(game,row,column)
            basicPopulate(game)

        #break
        #loop infinito se há itens com mais de uma possibilidade
    return game

#Return an array of coordinates inside array 'matrix' where 'number' is present
def getCoordinates(matrix,number):
    coordinates =[]
    for x in range(0,9):
        for y in range(0,9):
            if matrix[x][y] == number:
                coordinates.append( [x,y] )
    return coordinates

#popula o dicionário possibilities
def addPossibilitiesToDictionary(game,row,column):
    for number in range(1,10):
        #Verifica row, column and square
        if (isInsertable(game, row, column, number)):
            #print("Row ",row," Column ", column," N ",number)
            if (row,column) in possibilities: #Checa se a posição já existe no dicionário
                possibilities[(row,column)].append(number)
            else:
                possibilities[(row,column)] = [number]
            #print(possibilities)

#popula as coordenadas onde só ha 1 número possível
def basicPopulate(game):
    for key in possibilities:
        if len(possibilities[key]) == 1:
            game[key[0]][key[1]] = possibilities[key][0]
            
#verifica se há pares de possibilidades nas coordenadas dentro de um quadrado
#NÃO TESTADO
"""def pairPopulate(game):
    duoKeys = []
    for key in possibilities:
        #apenas dois valores possiveis para a coordenada
        #duo = possibilities[key] if (len(possibilities[key]) == 2) else []
        duoKeys.append(key) if (len(possibilities[key]) == 2) else []

    for square in squares:
        #containsMatchingMultipleDuoKeys(square,duoKeys):
        #   updateSquareValues"""

#NÃO TESTADO
def containsMatchingMultipleDuoKeys(square,duoKeys):
    duoKeysCounter = 0
    for coordinate in square:
        if arrayContains(duoKeys,coordinate):
            duoKeysCounter += 1

    
#NÃO TESTADO
def arrayContains(array,itemToCheck):
    for item in array:
        if itemToCheck == item:
            return True
    return False

