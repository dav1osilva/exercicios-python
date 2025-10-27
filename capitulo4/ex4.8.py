print("falopouco")
print("falomuito")
plano = input("Qual é o seu plano de celular? ")
if plano == "falopouco":
    minutos_plano = 100
    preço = 50
    custo_extra = 0.20
if plano == "falomuito":
    minutos_plano = 500
    preço = 99
    custo_extra = 0.15

minutos = float(input("Por quantos minutos você usou seu plano? "))
if plano == "falopouco": 
    if minutos > 100:
        total = preço + (minutos - 100) * custo_extra
    else:
        total = preço

if plano == "falomuito":
    if minutos > 500:
        total = preço  + (minutos - 500) * custo_extra
    else:
        total = preço

print(f"Você usou o plano {plano} e pagará um total de R$ {total:.2f}")

    

    