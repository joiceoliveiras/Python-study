# 4) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.

base  = int(input("Base: "))
expoente = int(input("Expoente: "))

result = 1
for i in range(expoente):
    result = result * base

print(result)
