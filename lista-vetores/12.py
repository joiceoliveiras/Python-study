#) Escreva um programa que leia um vetor de 10 elementos.
# Crie um segundo vetor, com todos os elementos na ordem inversa, ou seja, o último elemento passará a ser o primeiro,
# o penúltimo será o segundo e assim por diante.
# Por último, imprima os dois vetores.

vt_1 = []
vt_2 = []
for i in range(10):
    n = int(input(f"[Vetor 1] Digite o valor {i + 1} "))
    vt_1.append(n)
for i in range(10):
    vt_2 = vt_1[::-1]

print(vt_1)
print(vt_2)
