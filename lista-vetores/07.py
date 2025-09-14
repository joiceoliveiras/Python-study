#07) Escreva um programa que carregue uma lista com 10 valores inteiros. Em seguida, o programa deverá apresentar: 
#todos os valores que foram lidos; 
#todos os valores positivos; e 
#todos os valores negativos. 

valores = []

for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    valores.append(valor)

print("Valores lidos:", valores)

positivos = [v for v in valores if v > 0]
negativos = [v for v in valores if v < 0]

print("Valores positivos:", positivos)
print("Valores negativos:", negativos)
