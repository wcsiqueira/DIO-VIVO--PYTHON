import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # Lista de opções do menu, cada opção é uma tupla contendo a letra da opção e sua descrição.
    opcoes_menu = [
        ("d", "Depositar"),
        ("s", "Sacar"),
        ("e", "Exibir extrato"),
        ("nu", "Criar usuário"),
        ("nc", "Criar conta"),
        ("lc", "Listar contas"),
        ("q", "Sair"),
    ]

    # Loop principal que mantém o programa em execução até que o usuário escolha sair.
    while True:
        # Exibe o menu na tela para que o usuário possa ver as opções disponíveis.
        print("\n=== MENU ===")
        # Itera sobre a lista de opções do menu e imprime cada opção na tela.
        for opcao, descricao in opcoes_menu:
            print(f"{opcao}: {descricao}")

        # Solicita ao usuário que escolha uma opção do menu e armazena a escolha na variável 'opcao'.
        opcao = input("Escolha uma opção: ")

        # Utiliza a estrutura 'match' para realizar uma ação com base na opção escolhida pelo usuário.
        match opcao:
            # a opção escolhida seja 'd', realiza um depósito na conta.
            case "d":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            # a opção escolhida seja 's', realiza um saque na conta.
            case "s":
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )

            #  opção escolhida seja 'e', exibe o extrato da conta.
            case "e":
                exibir_extrato(saldo, extrato=extrato)

            #  opção escolhida seja 'nu', cria um novo usuário.
            case "nu":
                criar_usuario(usuarios)

            # opção escolhida seja 'nc', cria uma nova conta.
            case "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)

            # opção escolhida seja 'lc', lista todas as contas.
            case "lc":
                listar_contas(contas)

            # opção escolhida seja 'q', encerra o programa.
            case "q":
                break

            # opção escolhida não corresponda a nenhuma das opções anteriores, exibe uma mensagem de erro.
            case _:
                print(
                    "Operação inválida, por favor selecione novamente a operação desejada." )               )


main()
