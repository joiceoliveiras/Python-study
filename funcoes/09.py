#Implemente uma função chamada calcular_media_ponderada que recebe duas listas do mesmo tamanho como parâmetros: uma contendo as notas e outra contendo os pesos correspondentes, e retorna a média ponderada dessas notas.

def calcular_media_ponderada(notas, pesos):
    total_ponderado = 0
    soma_pesos = 0
    for i in range(len(notas)):
        total_ponderado += notas[i] * pesos[i]
        soma_pesos += pesos[i]
    return total_ponderado / soma_pesos if soma_pesos != 0 else 0
print(calcular_media_ponderada([8, 9, 7], [2, 3, 5]))