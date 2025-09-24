#Crie uma função chamada verificar_anagrama que recebe duas strings como parâmetro e retorna True se as duas #strings forem anagramas uma da outra, e False caso contrário.

def verificar_anagrama(str1, str2):
    return sorted(str1) == sorted(str2)
print(verificar_anagrama("amor", "roma"))
print(verificar_anagrama("casa", "saco"))