#13) Escreva um programa que leia 10 valores numéricos inteiros em um vetor e três números inteiros nas #variáveis A, B e C. Após carregar os valores do vetor, informe o número de vezes que os números A, B e C #aparecem no vetor.

vetor = []
a = 10
b = 20
c = 30

for i in range(11):
    n = int(input(f"Digite o valor {i + 1} "))
    vetor.append(n)
qtd_a = vetor.count(a)
qtd_b = vetor.count(b)
qtd_c = vetor.count(c)
print(f"Números no vetor: {vetor}")    
print(f"Quantidade de vezes que o {a} aparece: {qtd_a} vezes")
print(f"Quantidade de vezes que o {b} aparece: {qtd_b} vezes")
print(f"Quantidade de vezes que o {c} aparece: {qtd_c} vezes")
    