#4) Escreva um programa que deverá carregar o nome e a idade de 10 pessoas. Esses valores deverão ser armazenados #em duas listas separadas. Em seguida, o programa deverá apresentar uma lista com os nomes e as idades das #pessoas, sendo um ao lado do outro. Exemplo: 
#	Maria | 20 
# 	José | 10
#	Francisco | 15
#nomes = []
#idades = []

for i in range(4):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    nomes.append(nome)
    idades.append(idade)

print("\nLista de nomes e idades:")
for i in range(4):
    print(f"{nomes[i]} | {idades[i]}")
