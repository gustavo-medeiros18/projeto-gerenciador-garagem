from dao.carros_dao import ler_carros_arquivo, salvar_carros
from utils.carros_utils import encontrar_carro

def cadastrar_carro(placa, cor, modelo, ano):
    carro = {
        "placa": placa,
        "cor": cor,
        "modelo": modelo,
        "ano": ano
    }

    lista_carros = ler_carros_arquivo()
    lista_carros.append(carro)
    salvar_carros(lista_carros)
    print("\nCarro cadastrado com êxito")

def editar_carro(placa_busca, nova_placa, nova_cor, novo_modelo, novo_ano):
    lista_carros = ler_carros_arquivo()
    carro_existente = encontrar_carro(placa_busca, lista_carros)

    dicionario_atualizacao = {
        "placa": carro_existente["placa"],
        "cor": carro_existente["cor"],
        "modelo": carro_existente["modelo"],
        "ano": carro_existente["ano"]
    }

    if len(nova_placa) > 0:
        dicionario_atualizacao["placa"] = nova_placa
    
    if len(nova_cor) > 0:
        dicionario_atualizacao["cor"] = nova_cor

    if len(novo_modelo) > 0:
        dicionario_atualizacao["modelo"] = novo_modelo

    if novo_ano:
        dicionario_atualizacao["ano"] = novo_ano
        
    carro_existente["placa"] = dicionario_atualizacao["placa"]
    carro_existente["cor"] = dicionario_atualizacao["cor"]
    carro_existente["modelo"] = dicionario_atualizacao["modelo"]
    carro_existente["ano"] = dicionario_atualizacao["ano"]

    salvar_carros(lista_carros)

    print("\nCarro editado com êxito.")

def deletar_carro(carro_apagar):
    lista_carros = ler_carros_arquivo()

    lista_carros.remove(carro_apagar)
    salvar_carros(lista_carros)

    print("\nCarro deletado com êxito")