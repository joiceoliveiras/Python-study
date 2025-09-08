#Faça um programa que receba o total das vendas de cada #vendedor e armazene-os em um vetor. Receba também o #percentual de comissão de cada vendedor e armazene-o em #outro vetor. Receba os nomes desses vendedores e #armazene-os em um terceiro vetor. Utilize apenas dez #vendedores. Calcule e mostre:
#
#um relatório com os nomes dos vendedores e os valores a #receber;
#
#o total das vendas de todos os vendedores;
#
#o maior valor a receber e quem o receberá;
#
#o menor valor a receber e quem o receberá.
#
#Faça um programa que carregue um vetor com dez números #reais, calcule e mostre a quantidade de números negativos #e a soma dos números positivos desse vetor.

nomes = []
vendas = []
comissoes = []

for i in range(10):
    nome = input(f"Nome do vendedor {i+1}: ")
    venda = float(input(f"Total vendido pelo vendedor {nome}: "))
    comissao = float(input(f"Percentual de comissão de {nome} (em decimal, ex: 0.10 para 10%): "))
    
    nomes.append(nome)
    vendas.append(venda)
    comissoes.append(comissao)

valores_a_receber = [vendas[i] * comissoes[i] for i in range(10)]

print("Relatório de vendedores e valores a receber:")
for i in range(10):
    print(f"{nomes[i]}: R$ {valores_a_receber[i]:.2f}")

total_vendas = sum(vendas)
print(f"Total das vendas de todos vendedores: R$ {total_vendas:.2f}")

maior_valor = max(valores_a_receber)
menor_valor = min(valores_a_receber)
indice_maior = valores_a_receber.index(maior_valor)
indice_menor = valores_a_receber.index(menor_valor)

print(f"Maior valor a receber: R$ {maior_valor:.2f} - {nomes[indice_maior]}")
print(f"Menor valor a receber: R$ {menor_valor:.2f} - {nomes[indice_menor]}")
