#Soma dos elementos de cada linha (retorna lista com soma por linha)

matriz = [[1,2],[3,4]]
somas_linhas = []
for linha in matriz:
    soma = sum(linha)
    somas_linhas.append(soma)
print(somas_linhas)
