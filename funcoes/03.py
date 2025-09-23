#Desenvolva uma função chamada verificar_primo que 
# recebe um número inteiro como parâmetro e retorna 
# True se o #número for primo, e False caso contrário.

def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True