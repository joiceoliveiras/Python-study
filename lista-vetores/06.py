#6) Escreva um programa que deverá ler o nome e a nota de N alunos. O valor de N é informado através da entrada padrão. Em seguida o programa deverá apresentar: 
#O nome do aluno que tirou a maior nota; 
#Os nomes de todos os alunos que ficaram acima da média, considere a média 7,0; 
#Os nomes de todos os alunos que ficaram abaixo da média. 

N = int(input("Digite a quantidade de alunos: "))

nomes = []
notas = []

for i in range(N):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    nomes.append(nome)
    notas.append(nota)


maior_nota = notas[0]
nome_maior = nomes[0]
for i in range(1, N):
    if notas[i] > maior_nota:
        maior_nota = notas[i]
        nome_maior = nomes[i]


acima_media = []

abaixo_media = []

for i in range(N):
    if notas[i] > 7.0:
        acima_media.append(nomes[i])
    elif notas[i] < 7.0:
        abaixo_media.append(nomes[i])

print(f"\nAluno com maior nota: {nome_maior} ({maior_nota})\n")

print("Alunos acima da média 7.0:")
for nome in acima_media:
    print(nome)

print("\nAlunos abaixo da média 7.0:")
for nome in abaixo_media:
    print(nome)
