#Escreva uma função chamada contar_palavras que recebe uma string como parâmetro e retorna uma lista onde cada #item da lista é uma palavra encontrada juntamente com a quantidade de ocorrências dessa palavra na string #fornecida como parâmetro.


def contar_palavras(texto):
    palavras = texto.split()
    resultado = []
    palavras_vistas = set()
    for p in palavras:
        if p not in palavras_vistas:
            qtd = palavras.count(p)
            resultado.append(f"{p}({qtd})")
            palavras_vistas.add(p)
    return resultado
print(contar_palavras("O IFCE é 10"))