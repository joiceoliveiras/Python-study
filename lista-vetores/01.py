#1) Crie um programa que lê 5 valores inteiros da entrada padrão e armazene-os numa lista, em seguida, mostre na tela todos os valores que foram lidos.

valores = []

for i in range(5):
    n = int(input(f"Digite o valor {i + 1} "))
    valores.append(n)
print(valores)