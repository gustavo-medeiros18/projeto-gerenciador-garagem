def encontrar_carro(placa, lista_carros):
    carro_encontrado = None

    # placa recebida: cdc-2026
    # placa do carro cadastrado: cdc-2026

    for carro in lista_carros:
        if carro["placa"].lower() == placa.lower():
            carro_encontrado = carro
            break
    
    return carro_encontrado