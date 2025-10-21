matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
transposta = []
for i in range(len(matriz[0])):
    linha = []
    for j in range(len(matriz)):
        linha.append(matriz[j][i])
    transposta.append(linha)
print(transposta)
