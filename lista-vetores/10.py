#10) Escreva um programa que deverá ter 2 vetores (listas) A e B, cada um contendo 10 números inteiros lidos da #entrada padrão. Crie um terceiro vetor que também deverá ter 10 posições e deverá armazenar o valor #correspondente do vetor A multiplicado pelo valor do índice correspondente no vetor B. 

A = []
B = []

for i in range(10):
    A.append(int(input(f"Digite o {i+1}º número do vetor A: ")))
for i in range(10):
    B.append(int(input(f"Digite o {i+1}º número do vetor B: ")))

C = []

for i in range(10):
    C.append(A[i] * B[i])

print("Vetor C (A[i] * B[i]):", C)
