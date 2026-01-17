carros = []

def cadastrar_carro():
    placa = input("Digite a placa: ")
    cor = input("Digite a cor: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))

    carro = {
        "placa": placa,
        "cor": cor,
        "modelo": modelo,
        "ano": ano
    }

    carros.append(carro)
    print("\nCarro cadastrado com êxito")

def listar_carros():
    print("\n-------------------- LISTA DE CARROS --------------------")

    for carro in carros:
        print(f"Placa: {carro['placa']} | Modelo: {carro['modelo']} | Cor: {carro['cor']} | Ano: {carro['ano']}")
    
    print("---------------------------------------------------------")

def exibir_menu():
    print("\n---------- GERENCIADOR DE GARAGEM ----------")
    print("1 - Cadastrar um carro")
    print("2 - Listar os carros existentes")
    print("3 - Editar um carro")
    print("4 - Deletar um carro")
    print("5 - Sair")

while True:
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ")

    if opcao_escolhida == "1":
        cadastrar_carro()
    elif opcao_escolhida == "2":
        listar_carros()
    elif opcao_escolhida == "3":
        print("\nAinda vamos implementar essa funcionalidade")
    elif opcao_escolhida == "4":
        print("\nAinda vamos implementar essa funcionalidade")
    elif opcao_escolhida == "5":
        print("\nEncerrando o gerenciador de garagem. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente")