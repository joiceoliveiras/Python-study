#8) Escreva um programa em Python que deverá realizar a leitura do peso de várias pessoas. A condição de parada deverá ser quando for digitado um peso negativo. O programa deverá calcular e apresentar: a) soma de todos os pesos; b) a média dos pesos; c) o maior peso; e d) o menor peso.

soma = 0
quantidade = 0
maior_peso = None
menor_peso = None

while True:
    peso = float(input('Digite  o peso (valor negativo para sair)'))

    if peso < 0:
        break

    soma += peso
    quantidade += 1

    if maior_peso is None or peso > maior_peso:
        maior_peso = peso
    if menor_peso is None or peso < menor_peso:
        menor_peso = peso

if quantidade > 0:
    media = soma / quantidade
    print(f'Soma dos pesos: {soma}')
    print(f'Média dos pesos: {media}')
    print(f'Maior peso: {maior_peso}')
    print(f'Menor peso: {menor_peso}')