# 6) Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. 

total_alunos = 0
turmas = int(input('Quantidade de turmas: '))

for i in range(turmas):
    alunos = int(input(f'Total de alunos na Turma {i +1} '))

    while alunos > 40:
        print('A turma nao pode ter mais que 40 alunos')
        alunos = int(input(f'Total de alunos na Turma {i +1} '))

    total_alunos += alunos

media = total_alunos / turmas
print(f'A média de alunos por turma é: {media}')