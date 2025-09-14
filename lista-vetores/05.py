#5) Escreva um programa que deverá realizar a leitura do preço de diversos produtos. O programa deverá encerrar a #leitura quando for digitado um valor menor ou igual a zero. Após a leitura, o programa deverá apresentar todos os #preços que foram lidos, o maior e o menor preço.
#Atenção: O último valor lido não deverá ser considerado no cálculo, nem apresentado na tela. 

precos = []

while True:
    preco = float(input("Digite o preço do produto (ou 0 para sair): "))
    if preco <= 0:
        break
    precos.append(preco)

print("\nPreços digitados:")
for preco in precos:
    print(preco)

if precos:
    maior = precos[0]
    menor = precos[0]
    for preco in precos:
        if preco > maior:
            maior = preco
        if preco < menor:
            menor = preco
    print(f"Maior preço: {maior}")
    print(f"Menor preço: {menor}")
else:
    print("Nenhum preço válido foi informado.")
