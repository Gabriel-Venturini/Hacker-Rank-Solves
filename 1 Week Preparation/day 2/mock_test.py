def inversaoColuna(matrix, coluna):
    # linha, coluna
    novaMatrix = matrix # armazena matrix
    armazenaColuna = []
    armazenaValor = int
    for i in range(0, len(matrix)): # recebe valores da coluna
        armazenaColuna.append(matrix[i][coluna])
        # print(matrix[i][coluna])
    j = -1
    i = 0
    while i < len(armazenaColuna) / 2: # inverte coluna
        armazenaValor = armazenaColuna[j]
        armazenaColuna[j] = armazenaColuna[i]
        armazenaColuna[i] = armazenaValor
        i += 1
        j -= 1

    i = 0
    while i < len(armazenaColuna):
        novaMatrix[i][coluna] = armazenaColuna[i]
        i += 1
    
    return novaMatrix

def inversaoLinha(matrix, linha):
    novaMatrix = matrix
    armazenaLinha = matrix[linha]
    armazenaValor = int
    i = 0
    j = -1 # começa do ultimo elemento

    while i < len(armazenaLinha) / 2:
        armazenaValor = armazenaLinha[i]
        armazenaLinha[i] = armazenaLinha[j]
        armazenaLinha[j] = armazenaValor

        i += 1
        j -= 1
    
    novaMatrix[linha] = armazenaLinha
    return novaMatrix

def somaValores(matrix):
    # somar 2 por 2 ent 4 valores
    novaMatrix = matrix
    armazenaValores = []
    i = 0
    j = 0
    while j < 2: # roda primeira linha
        armazenaValores.append(novaMatrix[i][j])
        j += 1
    
    j = 0
    i = 1

    while j < 2: # segunda linha
        armazenaValores.append(novaMatrix[i][j])
        j += 1

    return sum(armazenaValores)

# codigo funcional

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

coluna = 0
linha = 0

colunaInvertida = inversaoColuna(matrix, coluna) # autoexplicativo

linhaInvertida = inversaoLinha(colunaInvertida, linha) # utiliza a matrix com a coluna ja invertida

total = somaValores(linhaInvertida)

print(total)