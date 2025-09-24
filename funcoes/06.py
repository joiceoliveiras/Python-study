#Crie uma função chamada soma_fatorial que recebe um número inteiro positivo como parâmetro e retorna a soma dos #fatoriais de todos os números de 1 até o número passado como parâmetro.

def soma_fatorial(n):
    def fatorial(x):
        f = 1
        for i in range(2, x+1):
            f *= i
        return f
    soma = 0
    for num in range(1, n+1):
        soma += fatorial(num)
    return soma
print(soma_fatorial(4))