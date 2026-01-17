carros = []

def encontrar_carro(placa):
    carro_encontrado = None

    # placa recebida: cdc-2026
    # placa do carro cadastrado: cdc-2026

    for carro in carros:
        if carro["placa"].lower() == placa.lower():
            carro_encontrado = carro
            break
    
    return carro_encontrado

def cadastrar_carro():
    placa = input("Digite a placa: ").strip()
    if len(placa) == 0:
        print("\nO campo placa não pode ser vazio.")
        return

    carro_existente = encontrar_carro(placa)
    if carro_existente != None:
        print("\nJá existe um carro cadastrado com essa placa.")
        return

    cor = input("Digite a cor: ").strip()
    if len(cor) == 0:
        print("\nO campo cor não pode ser vazio.")
        return

    modelo = input("Digite o modelo: ").strip()
    if len(modelo) == 0:
        print("\nO campo modelo não pode ser vazio.")
        return

    try:
        ano = int(input("Digite o ano: "))
    except ValueError:
        print("\nAno inválido. Digite apenas números.")
        return

    carro = {
        "placa": placa,
        "cor": cor,
        "modelo": modelo,
        "ano": ano
    }

    carros.append(carro)
    print("\nCarro cadastrado com êxito")

def listar_carros():
    if len(carros) == 0:
        print("\nNenhum carro cadastrado.")
        return

    print("\n-------------------- LISTA DE CARROS --------------------")

    for carro in carros:
        print(f"Placa: {repr(carro['placa'])} | Modelo: {repr( carro['modelo'])} | Cor: {repr(carro['cor'])} | Ano: {carro['ano']}")
    
    print("---------------------------------------------------------")

def editar_carro():
    placa = input("Digite a placa do carro a ser editado: ").strip()

    carro_existente = encontrar_carro(placa)

    if carro_existente == None:
        print("\nNão foi encontrado um carro com essa placa")
        return

    dicionario_atualizacao = {
        "placa": carro_existente["placa"],
        "cor": carro_existente["cor"],
        "modelo": carro_existente["modelo"],
        "ano": carro_existente["ano"]
    }

    print("\nPressione Enter para manter o valor atual.")

    nova_placa = input(f"Nova placa (atual: {carro_existente['placa']}): ").strip()

    # nova_placa = cdc-2026
    # carro_existente["placa"] = cdc-2026
    if (len(nova_placa)) > 0 and (nova_placa.lower() != carro_existente["placa"].lower()):
        if encontrar_carro(nova_placa) != None:
            print("\nJá existe um outro carro com essa placa.")
            return

        dicionario_atualizacao["placa"] = nova_placa
    
    nova_cor = input(f"Nova cor (atual: {carro_existente['cor']}): ").strip()
    if len(nova_cor) > 0:
        dicionario_atualizacao["cor"] = nova_cor

    novo_modelo = input(f"Novo modelo (atual: {carro_existente['modelo']}): ").strip()
    if len(novo_modelo) > 0:
        dicionario_atualizacao["modelo"] = novo_modelo

    novo_ano = input(f"Novo ano (atual: {carro_existente['ano']}): ")
    if len(novo_ano) > 0:
        try:
            dicionario_atualizacao["ano"] = int(novo_ano)
        except ValueError:
            print("\nAno inválido. Alterações ignoradas.")
            return

    carro_existente["placa"] = dicionario_atualizacao["placa"]
    carro_existente["cor"] = dicionario_atualizacao["cor"]
    carro_existente["modelo"] = dicionario_atualizacao["modelo"]
    carro_existente["ano"] = dicionario_atualizacao["ano"]

    print("\nCarro editado com êxito.")


def deletar_carro():
    placa = input("Digite a placa do carro a ser deletado: ").strip()

    carro_retornado = encontrar_carro(placa)

    if carro_retornado == None:
        print("\nNão foi encontrado um carro com essa placa")
        return
    
    carros.remove(carro_retornado)
    print("\nCarro deletado com êxito")

def exibir_menu():
    print("\n---------- GERENCIADOR DE GARAGEM ----------")
    print("1 - Cadastrar um carro")
    print("2 - Listar os carros existentes")
    print("3 - Editar um carro")
    print("4 - Deletar um carro")
    print("5 - Sair")

while True:
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ").strip()
    print(f"A opção escolhida foi {repr(opcao_escolhida)}")

    if opcao_escolhida == "1":
        cadastrar_carro()
    elif opcao_escolhida == "2":
        listar_carros()
    elif opcao_escolhida == "3":
        editar_carro()
    elif opcao_escolhida == "4":
        deletar_carro()
    elif opcao_escolhida == "5":
        print("\nEncerrando o gerenciador de garagem. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente")