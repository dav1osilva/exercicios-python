km_percorrido = float(input("Quantos km o carro percorreu? "))
dias = float(input("Quantos dias você ficou com o carro alugado? "))
custo = (km_percorrido * 0.15) + (dias * 60)
print(f"O custo total foi de R$ {custo:.2f}")