carros = [
    {
        "placa": "CDC-2026",
        "cor": "Verde",
        "modelo": "Corolla",
        "ano": 2026
    },
    {
        "placa": "IOF2V26",
        "cor": "Prata",
        "modelo": "Kwid",
        "ano": 2023
    },
    {
        "placa": "JSS-1214",
        "cor": "Preto",
        "modelo": "HB20",
        "ano": 2019
    }
]

def encontrar_carro(placa):
    carro_encontrado = None

    for carro in carros:
        if carro["placa"] == placa:
            carro_encontrado = carro
            break
    
    return carro_encontrado

carro_retornado = encontrar_carro("abc-2000")
print(carro_retornado)