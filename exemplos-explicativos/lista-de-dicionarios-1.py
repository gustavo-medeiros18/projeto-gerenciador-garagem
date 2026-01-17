lista_carros = []

carro_1 = {
    "placa": "CDC-2026",
    "cor": "Verde",
    "modelo": "Corolla",
    "ano": 2026
}
lista_carros.append(carro_1)

carro_2 = {
    "placa": "IOF2V26",
    "cor": "Prata",
    "modelo": "Kwid",
    "ano": 2023
}
lista_carros.append(carro_2)

carro_3 = {
    "placa": "JSS-1214",
    "cor": "Preto",
    "modelo": "HB20",
    "ano": 2019
}
lista_carros.append(carro_3)

print("Impressão padrão")
print(lista_carros)

print("\nImpressão mais formatada")
for carro in lista_carros:
    print(f"Placa: {carro['placa']} | Modelo: {carro['modelo']} | Cor: {carro['cor']} | Ano: {carro['ano']}")

print(f"\nTipo da lista: {type(lista_carros)}")

print("\nTipo de cada elemento da lista")
for carro in lista_carros:
    print(type(carro))