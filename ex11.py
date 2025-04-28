#Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um
#acréscimo de acordo com um percentual informado pelo usuário.


preco_custo = float(input('Digite o preço de custo do produto: '))
percentual_acrescimo = float(input('Digite o percentual de acrescimo: '))

valor_acrescimo = preco_custo * (percentual_acrescimo / 100)
preco_venda = preco_custo + valor_acrescimo

print("O valor de venda é: ", preco_venda)