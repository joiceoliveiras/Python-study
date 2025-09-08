#Faça um programa que carregue um vetor com o nome de sete alunos. Carregue um outro vetor com a média final desses alunos. Calcule e mostre:

#o nome do aluno com maior média (desconsiderar empates);
#
#para cada aluno que ainda não está aprovado, isto é, com #média menor que 7.0, mostrar quanto esse aluno precisa #tirar no exame para ser aprovado. Considere que a média #para aprovação no exame é 5.0.

nomes = []
medias = []

for i in range(7):
    nome = input(f"Nome do aluno {i+1}: ")
    media = float(input(f"Média final de {nome}: "))
    nomes.append(nome)
    medias.append(media)


maior_media = max(medias)
indice_maior = medias.index(maior_media)
print(f"Aluno com maior média: {nomes[indice_maior]} com média {maior_media}")

for i in range(7):
    if medias[i] < 7.0:
        exame_necessario = 5.0 * 2 - medias[i]
        print(f"{nomes[i]} precisa tirar {exame_necessario:.2f} no exame para ser aprovado")


