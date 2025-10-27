valido = True
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Escolha uma dentre as seguintes operações: +, -, * ou / ")

if operacao == "+":
    calculo = n1 + n2
elif operacao == "-":
    calculo = n1 - n2
elif operacao == "*":
    calculo = n1 * n2
elif operacao == "/":
    calculo = n1 / n2
else:
    print("Operação inválida")
    valido = False

if valido:
    print(f"O resultado da operação é igual a {calculo} ")
