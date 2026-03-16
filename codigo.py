# Para pode executar o projeto, primeiro é necessário
# ativar o ambiente virtual, e em seguida instalar
# a biblioteca tabulate, que é utilizada por ele.
# Isso pode ser feito através dos seguintes comandos
# no terminal, que precisa estar aberto na pasta
# do projeto:

# python -m venv .venv
# .\.venv\Scripts\activate
# python -m pip install tabulate

from tabulate import tabulate
from dao.carros_dao import ler_carros_arquivo
from utils.carros_utils import encontrar_carro
from services.carros_service import cadastrar_carro, editar_carro, deletar_carro
from interfaces.cli import exibir_carros_lista, exibir_carros_tabela, exibir_menu

while True:
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ").strip()
    print(f"A opção escolhida foi {repr(opcao_escolhida)}")

    if opcao_escolhida == "1":
        placa = input("Digite a placa: ").strip()
        if len(placa) == 0:
            print("\nO campo placa não pode ser vazio.")
            continue

        lista_carros = ler_carros_arquivo()
        carro_existente = encontrar_carro(placa, lista_carros)
        if carro_existente != None:
            print("\nJá existe um carro cadastrado com essa placa.")
            continue

        cor = input("Digite a cor: ").strip()
        if len(cor) == 0:
            print("\nO campo cor não pode ser vazio.")
            continue

        modelo = input("Digite o modelo: ").strip()
        if len(modelo) == 0:
            print("\nO campo modelo não pode ser vazio.")
            continue

        try:
            ano = int(input("Digite o ano: "))
        except ValueError:
            print("\nAno inválido. Digite apenas números.")
            continue
        cadastrar_carro(placa, cor, modelo, ano)
    elif opcao_escolhida == "2":
        exibir_carros_lista()
    elif opcao_escolhida == "3":
        exibir_carros_tabela()
    elif opcao_escolhida == "4":
        placa_busca = input("Digite a placa do carro a ser editado: ").strip()

        lista_carros = ler_carros_arquivo()
        carro_existente = encontrar_carro(placa_busca, lista_carros)

        if carro_existente == None:
            print("\nNão foi encontrado um carro com essa placa")
            continue

        print("\nPressione Enter para manter o valor atual.")

        nova_placa = input(f"Nova placa (atual: {carro_existente["placa"]}): ").strip()

        if (len(nova_placa)) > 0 and (nova_placa.lower() != carro_existente["placa"].lower()):
            if encontrar_carro(nova_placa, lista_carros) != None:
                print("\nJá existe um outro carro com essa placa.")
                continue
        
        nova_cor = input(f"Nova cor (atual: {carro_existente["cor"]}): ").strip()
        novo_modelo = input(f"Novo modelo (atual: {carro_existente["modelo"]}): ").strip()

        novo_ano = input(f"Novo ano (atual: {carro_existente["ano"]}): ")

        if len(novo_ano) > 0:
            try:
                novo_ano = int(novo_ano)
            except ValueError:
                print("\nAno inválido. Alterações ignoradas.")
                continue

        editar_carro(placa_busca, nova_placa, nova_cor, novo_modelo, novo_ano)
    elif opcao_escolhida == "5":
        placa = input("Digite a placa do carro a ser deletado: ").strip()

        lista_carros = ler_carros_arquivo()
        carro_retornado = encontrar_carro(placa, lista_carros)

        if carro_retornado == None:
            print("\nNão foi encontrado um carro com essa placa")
            continue
        deletar_carro(carro_retornado)
    elif opcao_escolhida == "6":
        print("\nEncerrando o gerenciador de garagem. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente")