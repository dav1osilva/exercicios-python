n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
operador = input("Escolha algum dos seguintes operadores: +, -, * ou / ")

if n2 == 0:
    print("Não é possível dividir por 0")
elif operador == "+":
    resultado = n1 + n2
elif operador == "-":
    resultado = n1 - n2
elif operador == "*":
    resultado = n1 * n2
else:
    resultado = n1 / n2

print(f"O resultado de {n1:.2f} {operador} {n2:.2f} = {resultado:.2f}")
