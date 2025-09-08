#3) Faça um Programa que faça a leitura de N números inteiros. O valor de N deve ser lido da entrada padrão. Após a leitura de cada um dos números, determine se ele é par ou ímpar, se ímpar verifique se ele é primo. 

qtd_numeros = int(input("Digite quantos números serão lidos: "))
for i in range(qtd_numeros):
    numero = int(input(f"Digite o {i + 1} número: "))
    if numero % 2 == 0:
        print(f'é par')
    else:
        eh_primo = True
        if numero < 2:
            eh_primo = False
        else: 
            for div in range(2, int(numero **0.5) + 1):
                if numero % div == 0:
                    eh_primo = False
                    break
        if eh_primo:
            print('é impar e primo')
        else:
            print('é impar, mas não é primo')