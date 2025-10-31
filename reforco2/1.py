n = float(input("Digite um valor: "))
tipo = input("Digite uma das seguintes unidades de medida: km, m, cm ou mm ")

conversao = {
    "km": 10 ** 6,
    "m": 10 ** 3,
    "cm": 10 ** 1,
    "mm": 10 ** 0
}

if tipo in conversao:
    resultado = n * conversao[tipo]
    print(f"{n} {tipo} = {resultado:.2f} mm")
else:
    print("Unidade de medida não identificada")