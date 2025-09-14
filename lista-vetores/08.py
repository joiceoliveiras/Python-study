#08) Escreva um programa que deverá conter três listas, cada uma contendo dez valores: a primeira possui o código #dos produtos; a segunda possui a descrição do produto; e a terceira lista possui o preço do produto. Sabe-se que #a empresa deverá realizar um reajuste de 10% no preço de todos os produtos que possuem código par; e um reajuste #de 20% em todos os produtos que possuem preço maior ou igual a R$ 1.000,00. No caso do produto satisfazer as duas #condições, ele deverá ter um aumento de 25%, ao invés de 30%. 
#	Observação: os valores das listas poderão ser atribuídos diretamente nas listas, sem a necessidade de #carregá-los da entrada padrão. 

codigos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
descricoes = ["Produto1", "Produto2", "Produto3", "Produto4", "Produto5",
              "Produto6", "Produto7", "Produto8", "Produto9", "Produto10"]
precos = [500, 1200, 350, 1050, 800, 1500, 250, 990, 2000, 750]

for i in range(10):
    codigo_par = (codigos[i] % 2 == 0)
    preco_alto = (precos[i] >= 1000)

    if codigo_par and preco_alto:
        precos[i] *= 1.25
    elif codigo_par:
        precos[i] *= 1.10
    elif preco_alto:
        precos[i] *= 1.20

print("Produtos após reajuste:")
for i in range(10):
    print(f"Código: {codigos[i]}, Descrição: {descricoes[i]}, Preço: R$ {precos[i]:.2f}")
