n = int(input("Digite um número: "))

if n < 0:
    print("Essa condição não se aplica aos números negativos")
elif n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é ímpar")
