"""A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de
uma compra e mostre o valor das prestações."""

valor_compra = float(input((f'Digite o valor da compra: '))) 
 
prestacao = valor_compra / 5 
 
print(f'5 parcelas de R$:  {prestacao}')