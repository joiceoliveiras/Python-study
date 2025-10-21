#matriz identidade (diagonal com 1, resto 0)
n = 4
matriz_identidade = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz_identidade.append(linha)
print(matriz_identidade)
