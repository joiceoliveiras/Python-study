#3) Escreva um programa que deverá realizar a leitura de N pesos informados pelo usuário. O valor de N é informado através da entrada padrão. Em seguida, o programa deverá: 
#Listar todos os pesos lidos
#Apresentar a soma de todos os pesos
#Apresentar a média dos pesos

N = int(input("Digite a quantidade de pesos que serão informados: "))

pesos = []

for i in range(N):
    peso = float(input(f"Digite o peso {i+1}: "))
    pesos.append(peso)

print("Pesos informados:", pesos)

soma = 0
for peso in pesos:
    soma = soma + peso

if N > 0:
    media = soma / N
else:
    media = 0

print("Soma dos pesos:", soma)
print("Média dos pesos:", media)



