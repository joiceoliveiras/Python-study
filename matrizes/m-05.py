A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]
soma = []
for i in range(len(A)):
    linha = []
    for j in range(len(A[0])):
        linha.append(A[i][j] + B[i][j])
    soma.append(linha)
print(soma)
#somar duas matrizes