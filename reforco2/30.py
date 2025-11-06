while True:
    n = int(input("Digite um número: "))
    if n < 0:
        break
    elif n == 0:
        print("Número 0 detectado")
    else:
        print("Número positivo detectado")

print("Número negativo detectado")