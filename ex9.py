"""Escreva um programa que receba as medidas dos 3 lados de um
triângulo e verifique se é possível sua formação.
condição de existência: Para construir um triângulo é necessário
que a medida de
qualquer um dos lados seja menor que a soma das medidas dos
outros dois e maior que o
valor absoluto da diferença entre essas medidas."""""

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))


if a < b + c and b < a + c and c < a + b:
    print("É possível formar um triângulo.")


    if a == b and b == c:
        print("Triângulo equilátero.")
    elif a != b and b != c and a != c:
        print("Triângulo escaleno.")
    else:
        print("Triângulo isósceles.")
else:
    print("Não é possível formar um triângulo.")
