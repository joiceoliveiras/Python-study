# 5) Faça um programa que realize 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
cont = 0
perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']

for pergunta in perguntas:
    resposta = input(f'{pergunta} ')
    if resposta == 'sim':
         cont += 1


if cont == 2:
    print('suspeita')
elif 3 <= cont <= 4:
    print('cumplice')
elif cont == 5:
    print('assasino')
else:
    print('inocente')

        