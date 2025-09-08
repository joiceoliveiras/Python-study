#Faça um programa que carregue três vetores com dez posições cada um. O primeiro vetor com os nomes de dez produtos, o segundo vetor com os códigos dos dez produtos e o terceiro vetor com os preços dos produtos. Mostre um relatório apenas com o nome, o código, o preço e o novo preço dos produtos que sofrerão aumento. Sabe-se que os produtos que sofrerão aumento são aqueles que possuem código por um preço superior a R$ 1.000,00. Sabe-se ainda que se o produto satisfaz as duas condições acima (código e preço), o aumento de preço será de 20%; se satisfaz apenas a condição de código, o aumento será de 15%; se satisfaz apenas a condição de preço, o aumento será de 10%.

nomes = []
codigos = []
precos = []

for i in range(10):
    nome = input(f"Nome do produto {i+1}: ")
    codigo = int(input(f"Código do produto {nome}: "))
    preco = float(input(f"Preço do produto {nome}: "))
    nomes.append(nome)
    codigos.append(codigo)
    precos.append(preco)

print("Relatório de produtos com aumento:")

for i in range(10):
    codigo_maior_1000 = codigos[i] > 1000
    preco_maior_1000 = precos[i] > 1000

    if codigo_maior_1000 and preco_maior_1000:
        novo_preco = precos[i] * 1.20
    elif codigo_maior_1000:
        novo_preco = precos[i] * 1.15
    elif preco_maior_1000:
        novo_preco = precos[i] * 1.10
    else:
        continue  # não sofre aumento

    print(f"Produto: {nomes[i]}, Código: {codigos[i]}, Preço antigo: R$ {precos[i]:.2f}, Novo preço: R$ {novo_preco:.2f}")
