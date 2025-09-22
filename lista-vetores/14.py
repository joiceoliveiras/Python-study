#14) Escreva um programa que deverá carregar da entrada 10 valores inteiros. Em seguida, o programa deverá ler #dois números inteiros: X e Y. O programa deverá percorrer o vetor substituindo todos os valores que são iguais #a X por Y. Por último, o programa deverá imprimir todos os valores do vetor na tela.

lista = []


for i in range(10):
    n = int(input(f"Digite o valor {i + 1} "))
    lista.append(n)
x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))

for i in range(len(lista)):
    if lista[i] == x:
        lista[i] = y
    
print(lista)