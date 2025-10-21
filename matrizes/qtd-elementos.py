#Contar quantos elementos têm um valor específico

matriz = [[1,2,3],[4,2,6],[7,8,2]]
valor = 2
contador = 0
for linha in matriz:
    for elemento in linha:
        if elemento == valor:
            contador += 1
print(f"O valor {valor} aparece {contador} vezes.")
