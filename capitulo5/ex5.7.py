n = int(input("Tabuada de: "))
inicio = int(input("Valor inicial: "))
final = int(input("Valor final: "))

while inicio <= final:
    print(f"{n} x {inicio} = {n * inicio}")
    inicio = inicio + 1
