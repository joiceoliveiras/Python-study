#Desenvolva uma função chamada buscar_elemento que recebe uma lista e um elemento como parâmetros e retorna True se o elemento estiver presente na lista, e False caso contrário.

def buscar_elemento(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
    return False
print(buscar_elemento([1, 2, 3, 4, 5], 3))
print(buscar_elemento(['a', 'b', 'c'], 'd'))