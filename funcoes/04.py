#Implemente uma função chamada contar_vogais 
#que recebe uma string como parâmetro 
#e retorna o número de vogais presentes nessa string.

def contar_vogais(texto):
    cont = 0
    for caractere in texto:
    
        if caractere in "aeiouAEIOU":
            cont += 1
    return cont
    
print(contar_vogais("Olá, tudo bem?"))