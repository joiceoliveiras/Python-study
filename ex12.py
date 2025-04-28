#Que bicho é esse?

print("Que bicho é esse?")

resposta = input("O animal é vertebrado? (sim/não): ")

if resposta == "sim":
    resposta2 = input("Tem sangue quente? (sim/não): ")
    
    if resposta2 == "sim":
        resposta3 = input("É mamífero? (sim/não): ")
        if resposta3 == "sim":
            print("É um urso!")
        else:
            print("É uma avestruz!")
    else:
        resposta3 = input("É peixe, réptil ou anfíbio? ")
        if resposta3 == "peixe":
            print("É um salmão!")
        elif resposta3 == "réptil":
            print("É uma tartaruga!")
        else:
            print("É uma rã!")
else:
    resposta2 = input("Tem pernas articuladas? (sim/não): ")
    
    if resposta2 == "sim":
        resposta3 = input("Tem 3 pares de pernas? (sim/não): ")
        if resposta3 == "sim":
            print("É uma formiga!")
        else:
            print("É um escorpião!")
    else:
        resposta3 = input("É vermiforme? (sim/não): ")
        if resposta3 == "sim":
            print("É uma minhoca!")
        else:
            print("É um trematódeo!")
