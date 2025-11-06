n = int(input("Digite um número: "))
contador = 1
a, b = 0, 1

while contador <= n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1