#Escreva uma função chamada inverter_string que 
#recebe uma string como parâmetro e retorna a mesma string invertida.

def inverter_string(texto):
    invertido = texto[::-1]
    return invertido
    
print(inverter_string("Pão"))