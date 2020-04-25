from datetime import date
from datetime import datetime

print("-" * 27)
print("Welcome the store CrazyRick")
print("-" * 27)

print("do register or login to enjoy the products")
print("\ndo register click 1")
print("do login click 2")
opcao = input("")

# caso as opções sejam digitadas erradas
if opcao != "1" and opcao != "2":
    while opcao != "1" and opcao != "2":
        print("-" * 50)
        print("Inválido, digite as opções informadas a cima!")
        print("-" * 50)
        opcao = input("Digite uma opção novamente:")

# para fazer o cadastro do sistema
if opcao == "1":

    nome = input("Usuario (COM SEIS NUMEROS):")
    qtd_letra_nome = len(nome)
    if qtd_letra_nome != 6:
        while qtd_letra_nome != 6:
            print("-" * 40)
            print("Inválido, usuário deve conter seis números!")
            print("-" * 40)
            nome = (input("Usuário:"))
            qtd_letra_nome = len(nome)
    print(nome)
    senha = input("Senha (COM SEIS NUMEROS):")

    if senha == nome:
        while senha == nome:
            print("-" * 40)
            print("A Senha não pode ser igual ao Usuário!")
            print("-" * 40)
            senha = input("Senha (COM SEIS NUMEROS):")
    qtd_senha = len(senha)
    if qtd_senha != 6:
        while qtd_senha != 6:
            print("Inválido, senha deve conter seis números!")
            senha = input("Senha (COM SEIS NÚMEROS):")
            qtd_senha = len(senha)

    cpf = input("CPF:")
    qtd_cpf = len(cpf)
    if qtd_cpf != 11:
        while qtd_cpf != 11:
            print("-" * 40)
            print("Inválido, CPF deve conter 11 numeros!")
            print("-" * 40)
            cpf = input("CPF:")
            qtd_cpf = len(cpf)

    data_nascimento = input("Data de nascimento DD/MM/AA:")
    qtd_nascimento = len(data_nascimento)
    if qtd_nascimento != 8:
        while qtd_nascimento != 8:
            print("-" * 50)
            print("Inválido, digite uma data com oito numeros!")
            print("-" * 50)
            data_nascimento = input("Data de nascimento:")
            qtd_nascimento = len(data_nascimento)

# entrando com o usuario já cadastrado
if opcao == "2":
    usuario = input("Login:")
    qtd_usuario = len(usuario)
    if qtd_usuario != 6:
        while qtd_usuario != 6:
            print("-" * 30)
            print("Login inválido, tente novamente!")
            print("-" * 30)
            usuario = input("Login:")
            qtd_usuario = len(usuario)

    senha = input("Senha:")
    qtd_senha = len(senha)
    if senha == usuario:
        while senha == usuario:
            print("-" * 30)
            print("Senha inválida, tente novamente!")
            print("-" * 30)
            senha = input("Senha:")
    if qtd_senha != 6:
        while qtd_senha != 6:
            print("-" * 30)
            print("Senha inválido, tente novamente!")
            print("-" * 30)
            senha = input("Senha:")
            while senha == usuario:
                print("-" * 30)
                print("Senha inválida, tente novamente!")
                print("-" * 30)
                senha = input("Senha:")
            qtd_senha = len(senha)

# cadastrando os produtos (Rick)
rick1 = "rick surfando"
rick2 = "rick em marte"
rick3 = "rick com pedrinha"
rick4 = "rick com chapeu"
rick5 = "rick pulando"

# valor do produto de pano (Rick)
_1 = float(230.00)
_2 = float(100.00)
_3 = float(80.00)
_4 = float(100.00)
_5 = float(400.0)

# cadastrando pro
boneco_ferro1 = ("morty na praia")
boneco_ferro2 = ("morty em las vegas")
boneco_ferro3 = ("Morty de ouro")
boneco_ferro4 = ("morty em casa")
boneco_ferro5 = ("morty em burao negro")

# escolher um produto para visualizar
print("[cod = 1] = Produtos de pano (Rick)")
print("[cod = 2] = Produtos de ferro (Morty)")
print("Digite o codigo do produto para ve-los:")
cod_produto = input()

# mostrando os produtos do cod 1
if cod_produto == "1":
    print("-" * 30)
    print("Rick no material de pano")
    print("-" * 30)
    print("RICK: \n1) {} = {}\n2) {} = {}\n3) {} = {}\n4) {} = {}\n5) {} = {}".format(rick1, _1,
                                                                                      rick2, _2,
                                                                                      rick3, _3, rick4, _4, rick5,
                                                                                      _5))
    print("-"*30)
    # escolhendo produto para compra
    n_produto = int(input("Digite o numero do produto que deseja compra-lo:"))
    if n_produto > 5:
        while n_produto > 5:
            print("-" * 30)
            print("Produto inválido, tente novamente!")
            print("-" * 30)
            cod_valor_produto = str("_ ")
            n_produto = int(input("Digite o numero do produto que deseja compra-lo:"))
    print("-"*30)
    qtd_produto = int(input("Deseja quantos desse produto:"))
    print("-"*30)
    if n_produto == 1:
        rick11 = rick1
        soma = _1 * qtd_produto
        print("O valor da sua compra é R${:.2f}".format(soma))
        print("-"*30)
        print(
            '- Parcelamento, somente em cartão de crédito!\n   * Valor até 1.500,00 reais, parcelamento máximo até 2x '
            'sem juros.')
        print("   * Valor acima de 1.500,00 reais, com parcelamentos acima de 3x com juros de 1,85 cada parcela.")
        print("-"*30)
        print("Escolhe uma forma de pagamento colocando o numero:")
        print("1)Crédito\n2)Débito\n3)Boleto")
        forma_pagamento = input("")
        print("-"*30)

        # pagamento em crédito até mil sem juros
        if forma_pagamento == "1":
            numero_parcela = int(input("Digite o numero de parcelas:"))
            if soma <= 1500:
                 if numero_parcela > 2:
                    while numero_parcela > 2:
                        print("Número de parcela máximo não permitido!")
                        numero_parcela = int(input("Digite o numero de parcelas:"))

            # pagamento até 12 vezes com 1.85 de juros em cada parcela
        if soma > 1500:
            # numero de parcela até 2 duas vezes sem juros
             if numero_parcela <= 2:
                 print("Valor da compra R${:.2f}".format(soma))
                if numero_parcela == 2:
                     soma = soma / numero_parcela
                      print("Valor em Parcelas: R${:.2f} de {}X".format(soma, numero_parcela))

                        # inserindo dados do cartão de crédito
                     numero_cartao = input("Numero do cartão:")
                     nome_cartao = input("Digite o nome impresso no cartão:")
                    cod_cartao = input("Código do cartão:")
                    valid_cartao = input("Validade:")

                     # compra realizada com sucesso
                     print("-" * 30)
                     print("Compra realizada com sucesso")
                     print("Produto: {}".format(rick11))
                    print("Valor da compra R${:.2f}".format(soma))
                    print("Valor em Parcelas: R${:.2f} de {}X".format(soma, numero_parcela))
                      data_hora_atual = datetime.now()
                      print(data_hora_atual.strftime("Data: %d/%m/%y\nHorário: %H:%M"))

                # numero de parcelas acima de 3 com juros
                if numero_parcela > 12:
                    while numero_parcela > 12:
                        print("Número de parcela máximo não permitido!")
                        numero_parcela = int(input("Digite o numero de parcelas:"))

                    juros_parcela = (((1.85 * numero_parcela) / 100) * soma)
                    soma_juros = juros_parcela + soma
                    soma = soma_juros / numero_parcela

                    print("Valor da compra R${:.2f}".format(soma_juros))
                    print("Valor em Parcelas: R${:.2f} de {}X".format(soma, numero_parcela))
                    print("-" * 30)

                    # inserindo dados do cartão de crédito
                    numero_cartao = input("Numero do cartão:")
                    nome_cartao = input("Digite o nome impresso no cartão:")
                    cod_cartao = input("Código do cartão:")
                    valid_cartao = input("Validade:")

                    print("-" * 30)
                    print("Compra realizada com sucesso")
                    print("Produto: {}".format(rick11))
                    print("Valor da compra R${:.2f}".format(soma_juros))
                    print("Valor em Parcelas: R${:.2f} de {}X".format(soma, numero_parcela))
                    data_hora_atual = datetime.now()
                    print(data_hora_atual.strftime("Data: %d/%m/%y\nHorário: %H:%M"))

    elif n_produto == 2:
        rick22 = rick2
        soma = _2 * qtd_produto
        print("O valor da sua compra é R${}".format(soma))
    elif n_produto == 3:
        rick33 = rick3
        soma = _3 * qtd_produto
        print("O valor da sua compra é R${}".format(soma))
    elif n_produto == 4:
        rick44 = rick4
        soma = _4 * qtd_produto
        print("O valor da sua compra é R${}".format(soma))
    elif n_produto == 5:
        rick55 = rick5
        soma = _5 * qtd_produto
