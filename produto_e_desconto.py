#faça um programa que receba o nome de um produto, seu valor e a quantidade comprada. após calcular o valor da compra, solicitar aplicação de desconto. exibir o nome do produto, o preço da compra e o valor total após a aplicação do desconto.

nome_prod = input(('Digite o nome do produto: '))
valor_prod = int(input('Digite o valor do produto: '))
qtd = int(input('Digite a quantidade: '))

valor_compra = valor_prod * qtd
desc = int(input('Desconto %: '))
total_desc = valor_compra - (valor_compra * desc / 100)

print('Produto: ', nome_prod, '\nPreço da compra: ', valor_compra, '\nTota com desconto: ', total_desc)