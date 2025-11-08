n = int(input("Digite um número: "))
contador = 1

while contador <= n:
    x = 1
    while x <= contador:
        print(x, end=" ")
        x += 1
    print()
    contador += 1