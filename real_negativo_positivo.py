#Faça um programa que carregue um vetor com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

numeros = []
for i in range(10):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

quant_negativos = sum(1 for n in numeros if n < 0)
soma_positivos = sum(n for n in numeros if n > 0)

print(f"Quantidade de números negativos: {quant_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
