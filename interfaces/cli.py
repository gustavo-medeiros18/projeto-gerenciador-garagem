from tabulate import tabulate
from dao.carros_dao import ler_carros_arquivo

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