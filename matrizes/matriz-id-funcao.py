def identidade(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(1 if i == j else 0)
        matriz.append(linha)
    return matriz

print(identidade(5))
