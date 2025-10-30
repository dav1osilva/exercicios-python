n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
contador = 1
resultado = 0

while contador <= n2:
    resultado += n1
    contador += 1
print(f"{n1} x {n2} = {resultado}")
