n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

if n1 == n2 == n3:
    print("Todos são iguais")
else:
    print(f"{maior:.2f} é o maior e {menor:.2f} é o menor")