valido = True
kwh = int(input("Quantos kwh foram consumidos? "))
instalacao = input("Qual tipo de instalação você tem? ")

if instalacao == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65

elif instalacao == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif instalacao == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60

else:
    print("Instalação desconhecida")
    valido = False

if valido:
    print(f"Você usou {kwh} kwh e tem a instalação tipo {instalacao}, então o custo é de R$ {preco:.2f}")