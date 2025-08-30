#Faça um programa que receba a quantidade em ml de água para encher um balde. Permita a repetição da operação de entrada até que seja atingido o limite de 1000ml.
balde = 0
while balde < 1000:
    qtd_agua = int(input('Digite a quantidade de água para preencher o balde (em ml):' ))
    balde += qtd_agua
    print(f'Quantidade atual no balde: {balde}ml')
print('Balde cheio')

