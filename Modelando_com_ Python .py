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


# corrgido na resolução anteriormente havia conflito  com a função depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def depositar(saldo, valor, extrato):
    """
       Realiza um depósito na conta do cliente.
    O que era esperado na saida não estava ocorrendo e foi solucionado junto a resolução
       Returns:
           saldo (float): Saldo atualizado da conta.
           extrato (str): Histórico de transações atualizado da conta.
    """

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


# Função corrigida na Resolução do Desafio
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
    """
    Função principal do programa que simula um sistema bancário.
    """

    # Constantes
    LIMITE_SAQUES = 5  # Limite de saques diários
    AGENCIA = "0001"  # Código da agência

    # Variáveis
    saldo = 0  # Inicia com  Saldo da conta
    limite = 1200  # Limite da conta
    extrato = ""  # Histórico de transações
    numero_saques = 0  # Número de saques realizados no dia
    usuarios = []  # Lista de usuários cadastrados
    contas = []  # Lista de contas

    # Menu principal
    opcoes_menu = [
        ("d", "Depositar"),
        ("s", "Sacar"),
        ("e", "Exibir extrato"),
        ("nu", "Criar usuário"),
        ("nc", "Criar conta"),
        ("lc", "Listar contas"),
        ("q", "Sair"),
    ]

    # Loop principal
    while True:
        # Exibir menu
        print("\n=== MENU ===")
        for opcao, descricao in opcoes_menu:
            print(f"{opcao}: {descricao}")

        # Obter escolha do usuário
        opcao = input("Escolha uma opção: ")

        # Processar escolha do usuário
        match opcao:
            case "d":
                # Depositar
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            case "s":
                # Sacar
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )

            case "e":
                # Exibir extrato
                exibir_extrato(saldo, extrato=extrato)

            case "nu":
                # Criar usuário
                criar_usuario(usuarios)

            case "nc":
                # Criar conta
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)

            case "lc":
                # Listar contas
                listar_contas(contas)

            case "q":
                # Sair
                break

            case _:
                # Opção inválida
                print(
                    "Operação inválida, por favor selecione novamente a operação desejada."
                )


main()
