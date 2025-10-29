n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
maior = max(n1, n2)
menor = min(n1, n2)

if maior == menor:
    print("Ambos são iguais")
else: 
    print(f"{maior:.2f} é maior e {menor:.2f} é menor")