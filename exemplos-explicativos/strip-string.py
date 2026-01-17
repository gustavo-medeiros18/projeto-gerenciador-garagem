placa = "  CDC-2026     "
modelo = "HB20     "

print("Sem tratamento com strip")
print(repr(placa))
print(repr(modelo))

print("\nCom tratamento com strip")

placa_tratada = repr(placa.strip())
modelo_tratado = repr(modelo.strip())

print(placa_tratada)
print(modelo_tratado)

cor = input("\nInforme uma cor para o carro: ")
print("Cor sem tratamento com strip:", repr(cor))

cor = input("\nInforme outra cor para o carro: ").strip()
print("Cor com tratamento com strip:", repr(cor))