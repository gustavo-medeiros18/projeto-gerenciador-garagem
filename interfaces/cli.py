from tabulate import tabulate
from dao.carros_dao import ler_carros_arquivo
from utils.carros_utils import encontrar_carro
from services.carros_service import cadastrar_carro, editar_carro, deletar_carro

def exibir_carros_lista():
    lista_carros = ler_carros_arquivo()

    if len(lista_carros) == 0:
        print("\nNenhum carro cadastrado.")
        return

    print("\n-------------------- LISTA DE CARROS --------------------")

    for carro in lista_carros:
        print(f"Placa: {repr(carro["placa"])} | Modelo: {repr( carro["modelo"])} | Cor: {repr(carro["cor"])} | Ano: {carro["ano"]}")
    
    print("---------------------------------------------------------")

def exibir_carros_tabela():
    lista_carros = ler_carros_arquivo()

    if len(lista_carros) == 0:
        print("\nNenhum carro cadastrado.")
        return

    print("\n------------ TABELA DE CARROS ------------")

    tabela = tabulate(lista_carros, headers="keys", tablefmt="fancy_grid")
    print(tabela)

def exibir_menu():
    print("\n---------- GERENCIADOR DE GARAGEM ----------")
    print("1 - Cadastrar um carro")
    print("2 - Exibir os carros existentes (lista)")
    print("3 - Exibir os carros existentes (tabela)")
    print("4 - Editar um carro")
    print("5 - Deletar um carro")
    print("6 - Sair")

def entrada_cadatrar_carro():
    placa = input("Digite a placa: ").strip()
    if len(placa) == 0:
        print("\nO campo placa não pode ser vazio.")
        return

    lista_carros = ler_carros_arquivo()
    carro_existente = encontrar_carro(placa, lista_carros)
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
    cadastrar_carro(placa, cor, modelo, ano)

def entrada_editar_carro():
    placa_busca = input("Digite a placa do carro a ser editado: ").strip()

    lista_carros = ler_carros_arquivo()
    carro_existente = encontrar_carro(placa_busca, lista_carros)

    if carro_existente == None:
        print("\nNão foi encontrado um carro com essa placa")
        return

    print("\nPressione Enter para manter o valor atual.")

    nova_placa = input(f"Nova placa (atual: {carro_existente["placa"]}): ").strip()

    if (len(nova_placa)) > 0 and (nova_placa.lower() != carro_existente["placa"].lower()):
        if encontrar_carro(nova_placa, lista_carros) != None:
            print("\nJá existe um outro carro com essa placa.")
            return
    
    nova_cor = input(f"Nova cor (atual: {carro_existente["cor"]}): ").strip()
    novo_modelo = input(f"Novo modelo (atual: {carro_existente["modelo"]}): ").strip()

    novo_ano = input(f"Novo ano (atual: {carro_existente["ano"]}): ")

    if len(novo_ano) > 0:
        try:
            novo_ano = int(novo_ano)
        except ValueError:
            print("\nAno inválido. Alterações ignoradas.")
            return

    editar_carro(placa_busca, nova_placa, nova_cor, novo_modelo, novo_ano)

def entrada_deletar_carro():
    placa = input("Digite a placa do carro a ser deletado: ").strip()

    lista_carros = ler_carros_arquivo()
    carro_retornado = encontrar_carro(placa, lista_carros)

    if carro_retornado == None:
        print("\nNão foi encontrado um carro com essa placa")
        return
    deletar_carro(carro_retornado)