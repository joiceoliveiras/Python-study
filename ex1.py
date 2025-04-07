# Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

nome = input('Nome do aluno: ')
print('Digite as 3 notas: ')
n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3)/3

print(f'A média do aluno: {nome} é: {media}')