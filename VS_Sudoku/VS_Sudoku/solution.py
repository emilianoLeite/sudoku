from generation import isInsertable, getSquaresDic, getSquareCoord

squares = getSquaresDic()
possibilities = {} #armazena todas as possibilidades de cada coordenada

def solveGame(game):
    while True: 
        coordinates = getCoordinates(game,0) #coordenadas que faltam ser preenchidas
        #print(coordinates)
        if not coordinates:
            break

        possibilities.clear()
        for row,column in coordinates: 
            populatePossibilities(game,row,column)
        
        #basicPopulate(game)
        pairPopulate(game)

        #break
        #loop infinito se itens com mais de uma possibilidade
    return game

#Return an array of coordinates inside array 'matrix' where 'number' is present
def getCoordinates(matrix,number):
    coordinates =[]
    for x in range(0,9):
        for y in range(0,9):
            if matrix[x][y] == number:
                coordinates.append( [x,y] )
    return coordinates

def populatePossibilities(game,row,column):
    for number in range(1,10):
        #Verifica row, column and square
        if (isInsertable(game, row, column, number)):
            print("Row ",row," Column ", column," N ",number)
            if (row,column) in possibilities: 
                possibilities[(row,column)].append(number)
            else:
                possibilities[(row,column)] = [number]
            print(possibilities)

def basicPopulate(game):
    for key in possibilities:
        if len(possibilities[key]) == 1:
            game[key[0]][key[1]] = possibilities[key][0]
            
#Nao TESTADO
def pairPopulate(game):
    duoKeys = []
    alreadyChecked = []
    for key in possibilities:
        if not key in alreadyChecked:
            #apenas dois possibilidades para a coordenada
            if (len(possibilities[key]) == 2):
                #alreadyChecked.append(key)
                duo = possibilities[key] #os dois valores possiveis
                square = getSquareCoord(key) #array com todas as coordenadas do quadrado onde duo se encontra
                moreDuos = hasMultiplePairs(square,duo)#array com as coordenadas onde o mesmo par de duo ocorre(incluindo a ocorrencia original)
                if len(moreDuos) > 1: #existem outros pares identicos, alem do original
                    for coord in moreDuos:
                        alreadyChecked.append(coord)
                    #moreDuos.append(key) #adiciona a coordenada inicial, para completar a lista
                    for coord in square: #varre todas as coordenadas do quadardo
                        if not coord in moreDuos: #verifica todos as outras coordenadas do quadrado
                            if duo[0] in possibilities[coord]:
                                possibilities[coord].remove(duo[0]) 
                            if duo[1] in possibilities[coord]:
                                possibilities[coord].remove(duo[1])  
    


#Nao TESTADO
def hasMultiplePairs(square,duo):
    pairs =[]
    for coordinate in square:
        if possibilities[coordinate] == duo:
            pairs.append(coordinate)
    return pairs