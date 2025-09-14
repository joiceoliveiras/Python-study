#2) Escreva um programa em Python que possua a lista denominada L e que armazene 5 números inteiros.
#O programa deve executar os seguintes passos: 
#a) Atribua os seguintes valores a esta lista: 1, 0, 5, -2, -5. 
#b) Armazene em uma variável inteira (simples) a soma entre os valores das posições L[0], L[1] e L[4] da lista e #ostre na tela esta soma. 
#c) Modifique a posição 4 da lista, atribuindo a esta posição o valor 50. 
#d) Mostre na tela cada valor da lista L, um em cada linha.

l = [1, 0, 5, -2, -5]

soma = l[0] + l[1] + l[4]

l[4] = 50


print(soma)
for lista in (l):
    print(lista)