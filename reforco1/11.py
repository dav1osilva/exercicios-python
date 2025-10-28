n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
contador = 1
resultado = 0

while contador <= n2:
    resultado += n1
    contador += 1

print(f"{n1:.2f} x {n2:.2f} = {resultado:.2f}")