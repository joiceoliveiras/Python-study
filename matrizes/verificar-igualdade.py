A = [[1,2],[3,4]]
B = [[1,2],[3,4]]
iguais = True
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] != B[i][j]:
            iguais = False
            break
print("Matrizes iguais?" , iguais)
