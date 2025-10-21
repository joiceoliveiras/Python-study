#Substituir todos os valores de uma matriz por outro valor

matriz = [[1,2,3],[4,5,6]]
novo_valor = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = novo_valor
print(matriz)
