# 1) Faça um programa que pergunte o preço de dois produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

prod_1 = float(input('Preço do produto 1: '))
prod_2 = float(input('Preço do produto 2: '))

if prod_1 < prod_2:
    print(f'Produto 1 com valor de {prod_1} R$ é o mais barato (compre este)')
elif prod_1 == prod_2:
    print(f'Os produtos tem o mesmo preço: (Produto 1 {prod_1} R$ e Produto 2 {prod_2} R$ (compre qualquer um)')
else:
    print(f'Produto 2 com valor de {prod_2} R$ é o mais barato (compre este)')