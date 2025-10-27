valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o seu salário? "))
anos_a_pagar = int(input("Por quantos você pagará a casa? "))
prestacao = valor_casa / (anos_a_pagar * 12)

if prestacao < (30 / 100 * salario):
    print("Empréstimo bancário aprovado")
else:
    print("Empréstimo desaprovado")