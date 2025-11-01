n = int(input("Digite um número: "))

for fator in range(1, 11):
    produto = n * fator
    print(f"{n} x {fator} = {produto}")
    