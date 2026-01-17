placa = "   CdC-2026    "
modelo = "   Hb20 "

print("Placa e modelo antes de qualquer tratamento")
print(repr(placa))
print(repr(modelo))

# placa = 'CdC-2026'
placa = placa.strip()
# modelo = 'Hb20'
modelo = modelo.strip()

print("\nPlaca e modelo após tratamento com strip")
print(repr(placa))
print(repr(modelo))

# placa = 'cdc-2026'
placa = placa.lower()
# modelo = 'hb20'
modelo = modelo.lower()

print("\nPlaca e modelo após tratamento com lower")
print(placa)
print(modelo)