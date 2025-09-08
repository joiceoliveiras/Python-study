#7) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

total_eleitores = int(input('Número de eleitores: '))
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

for i in range(total_eleitores):
    voto = int(input(f'Eleitor {i + 1}, digite seu voto (1, 2 ou 3)'))

    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1
    else:
        print('voto inválido')

    print('Resultado: ')
    print(f'Candidato 1: {votos_candidato_1} votos')
    print(f'Candidato 2: {votos_candidato_2} votos')
    print(f'Candidato 3: {votos_candidato_3} votos')