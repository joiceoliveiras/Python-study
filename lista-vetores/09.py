#09) Escreva um programa que deverá receber o preço e o nome de 5 produtos. Calcule e mostre: 
#
#a) A quantidade de produtos  com preço maior que R$ 100,00; 
#b) A quantidade de produtos com preço inferior a R$ 50,00; e 
#a) A média dos preços dos produtos cujo nome é Refrigerante.

nomes = []
precos = []

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    nomes.append(nome)
    precos.append(preco)

qtd_maior_100 = 0
qtd_menor_50 = 0
soma_refrigerante = 0
qtd_refrigerante = 0

for i in range(5):
    if precos[i] > 100:
        qtd_maior_100 += 1
    if precos[i] < 50:
        qtd_menor_50 += 1
    if nomes[i].lower() == "refrigerante":
        soma_refrigerante += precos[i]
        qtd_refrigerante += 1

media_refrigerante = soma_refrigerante / qtd_refrigerante if qtd_refrigerante > 0 else 0

print(f"Quantidade de produtos com preço > R$100: {qtd_maior_100}")
print(f"Quantidade de produtos com preço < R$50: {qtd_menor_50}")
print(f"Média dos preços dos produtos \"Refrigerante\": R$ {media_refrigerante:.2f}")
