soma = 0
matriz = [
    [1, 2, 3, 7],
    [4, 5, 6, 8],
]

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        soma += matriz[l][c]
print(soma)