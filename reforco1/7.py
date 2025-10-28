n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

if n2 == 0:
    print("Erro: não é possível dividir por 0")
else:
    print(f"{n1:.2f} / {n2:.2f} = {n1 / n2:.2f}")