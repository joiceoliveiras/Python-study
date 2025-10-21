matriz = [
    [1, 9, 3],
    [4, 5, 8],
    [7, 2, 6]
]
maior = matriz[0][0]
posicao = (0, 0)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            posicao = (i, j)
print("Maior:", maior, "Posição:", posicao)
