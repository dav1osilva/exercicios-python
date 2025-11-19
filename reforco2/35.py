n = int(input("Digite a quantidade de termos da sequência de Fibonacci desejada: "))
a, b = 0, 1
contador = 1

while contador <= n:
    print(a, end =" ")
    a, b = b, a + b
    contador += 1


