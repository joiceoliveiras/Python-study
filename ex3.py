"""Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final
do mês."""

nome = input('digite o nome do vendedor: ')
salario_fixo = float(input(f'Olá {nome} Digite o salário fixo: '))
total_vendas = float(input(f'Digite o total de vendas: '))
comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao
print(f'Relatório final: ')
print(f'Nome: {nome}')
print(f'Salário fixo, {salario_fixo}')
print(f'Salário final, {salario_final}')