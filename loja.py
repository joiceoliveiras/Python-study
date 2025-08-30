import os
os.system('cls' if os.name == 'nt' else 'clear')

usuarios = {'exemplo': '123'}
carrinho = []

def login():
    usuario_cadastrado = input('digite seu nome: ')
    senha_usuario_cadastrado = input('digite sua senha: ')
    if usuario_cadastrado in usuarios and usuarios[usuario_cadastrado] == senha_usuario_cadastrado:
        print('Login realizado com sucesso')
        return True
    else:
        print('usuário ou senha incorretos')
        return False

def cadastro():
    nome = input('Digite um nome para cadastro: ')
    if nome in usuarios:
        print('já cadastrado, faça o login')
        return False
    senha = input('Crie uma senha: ')
    usuarios[nome] = senha
    print('cadastro realizado')
    return True
def editar_cadastro():
    nome = input('Digite seu nome para editar cadastro: ')
    if nome not in usuarios:
        print('Usuário não encontrado. Cadastre-se primeiro.')
        return False
    senha_atual = input('Digite sua senha atual: ')
    if usuarios[nome] != senha_atual:
        print('Senha incorreta.')
        return False
    nova_senha = input('Digite a nova senha: ')
    usuarios[nome] = nova_senha
    print('Senha atualizada com sucesso.')
    return True

def menu():
    print('Loja aberta - Bem-vindo(a) ...')
    escolhas = input('Escolha uma opção\n 1 - EDITAR CADASTRO DE USUÁRIO\n 2 - VER CARRINHO\n 3 - COMPRAR\n 4 - FINALIZAR COMPRA\n 0 - SAIR\n')
    return escolhas

produtos = {
    "(1) - CAMISA": 45.99,
    "(2) - VESTIDO": 79.9,
    "(3) - BOLSA": 37.85,
    "(4) - SAPATO": 102.96,
    "(5) - CALÇA": 79.84
}

def exibir_produtos():
    for produto, preco in produtos.items():
        print(f"{produto}: R${preco:.2f}")

def comprar():
    exibir_produtos()
    try:
        escolha = int(input('Escolha o produto para compra: '))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return
    chave = f"({escolha}) - "
    produto_selecionado = None
    for p in produtos:
        if p.startswith(chave):
            produto_selecionado = p
            break
    if produto_selecionado:
        carrinho.append(produto_selecionado)
        preco = produtos[produto_selecionado]
        print(f'{produto_selecionado} - R${preco:.2f} adicionado ao carrinho')
    else:
        print("Produto inválido.")

def ver_carrinho():
    if not carrinho:
        print('Carrinho vazio')
        return
    print('Carrinho:')
    total = 0
    for item in carrinho:
        preco = produtos[item]
        total += preco
        print(f"{item} - R${preco:.2f}")
    print(f"Total: R${total:.2f}")

def finalizar_compra():
    if not carrinho:
        print("Seu carrinho está vazio.")
    else:
        ver_carrinho()
        print("Compra finalizada. Obrigado!")
        carrinho.clear()

while True:
    escolha = input('Escolha uma opção: 1 - Logar 2 - Cadastrar 0 - Sair\n').strip()
    if escolha == '1':
        if login():
            while True:
                opcao = menu()
                if opcao == '1':
                    editar_cadastro()
                elif opcao == '2':
                    ver_carrinho()
                elif opcao == '3':
                    comprar()
                elif opcao == '4':
                    finalizar_compra()
                elif opcao == '0':
                    print('Saindo do sistema...')
                    break
                else:
                    print('Opção inválida')
    elif escolha == '2':
        cadastro()
    elif escolha == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida')
