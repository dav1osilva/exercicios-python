n1 = int(input("Digite um número: "))
fator = int(input("Digite outro número: "))
contador = 1
produto = 0

while contador <= fator:
    produto += n1
    contador += 1

print(f"{n1} x {fator} = {produto}")