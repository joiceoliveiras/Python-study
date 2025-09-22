#Escreva um programa que leia da entrada padrão dois vetores de números inteiros com 10 números cada.
# Depois de carregá-los, gere um terceiro vetor formado pela diferença dos dois vetores lidos;
# um quarto vetor composto pela soma dos dois vetores lidos e por último um quinto vetor
# formado pela multiplicação dos dois vetores lidos.

v_1 = []
v_2 = []
diferenca = []
soma = []
mult = []

for i in range(10):
    n = int(input(f"[Vetor 1] Digite o valor {i + 1} "))
    v_1.append(n)

for i in range(10):
    n_2 = int(input(f"[Vetor 2] Digite o valor {i + 1} "))
    v_2.append(n_2)
for i in range(10):
    diferenca.append(v_1[i] - v_2[i])

for i in range(10):
    soma.append(v_1[i] + v_2[i])

for i in range(10):
    mult.append(v_1[i] * v_2[i])

print(f'Vetor 1: ', v_1)
print(f'Vetor 2: ', v_2)
print(f'Diferença: ', diferenca)
print(f'Soma: ', soma)
print(f'Multiplicação: ', mult)