#Crie uma função chamada calcular_area_retangulo que recebe a base e a altura de um retângulo como parâmetros e #retorna a área desse retângulo.

def calcular_area_retangulo(base, altura):
    return base * altura
   
base = int(input("Base: "))
altura = int(input("Altura: "))

area = calcular_area_retangulo(base, altura)
   
print(f"A área do retangulo é: {area}")