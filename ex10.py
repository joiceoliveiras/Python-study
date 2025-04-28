#Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2



print(f'A soma de: {num1} + {num2} = {soma}')
print(f'A subtração de: {num1} - {num2} = {sub}')
print(f'A multiplicação de: {num1} * {num2} = {mult}')

if num2 != 0:
    print(f'A divisão de: {num1} / {num2} = {div}')
else:
    print('Indefinida, divisão por zero não permitida')