memoria = None
uso = 0
resultado_atual = None

print("Calculadora")

while True:
    mostrar_memoria = uso >= 1
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz")
    if mostrar_memoria:
        print("MS - Salvar valor na memória")
        print("MR - Recuperar valor da memória")
        print("MC - Limpar memória")
    print("EXIT - Sair da calculadora")

    op = input("Opção: ").strip().upper()
    if op == 'EXIT':
        print("Encerrando a calculadora. Até mais!")
        break

    if mostrar_memoria and op in ['MS', 'MR', 'MC']:
        if op == 'MS':
            if resultado_atual is not None:
                memoria = resultado_atual
                print(f"Valor {memoria} salvo na memória.")
            else:
                print("Nenhum valor para salvar na memória.")
        elif op == 'MR':
            if memoria is not None:
                print(f"Valor na memória: {memoria}")
            else:
                print("Memória vazia.")
        elif op == 'MC':
            memoria = None
            print("Memória limpa.")
        continue

    try:
        if resultado_atual is None:
            n1 = float(input("Digite o primeiro número: "))
        else:
            n1 = resultado_atual

        if op in ['1', '2', '3', '4', '5', '6']:
            if op == '6':
                n2 = float(input("Digite o índice da raiz (ex: 2 para raiz quadrada): "))
            else:
                n2 = float(input("Digite o segundo número: "))

            if op == '1':
                resultado = n1 + n2
            elif op == '2':
                resultado = n1 - n2
            elif op == '3':
                resultado = n1 * n2
            elif op == '4':
                if n2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                    continue
                resultado = n1 / n2
            elif op == '5':
                resultado = n1 ** n2
            elif op == '6':
                if n2 <= 0:
                    print("Erro: índice da raiz deve ser positivo.")
                    continue
                if n1 < 0 and n2 % 2 == 0:
                    print("Erro: raiz par de número negativo não é real.")
                    continue
                resultado = n1 ** (1 / n2)

            print(f"Resultado: {resultado}")
            resultado_atual = resultado
            uso += 1
        else:
            print("Opção inválida. Tente novamente.")

    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
