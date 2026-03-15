import json

def ler_carros_arquivo():
    try:
        with open("carros.json", "r") as arquivo_json:
            lista_convertida = json.load(arquivo_json)
            return lista_convertida
    except FileNotFoundError:
        print("Primeira execução. Arquivo vazio ou inexistente.")

        lista_convertida = []
        return lista_convertida
    except json.decoder.JSONDecodeError:
        print("Conteúdo do arquivo não pode ser convertido.")

        lista_convertida = []
        return lista_convertida

def salvar_carros(lista_carros):
    with open("carros.json", "w") as arquivo_json:
        json.dump(lista_carros, arquivo_json, indent=2)