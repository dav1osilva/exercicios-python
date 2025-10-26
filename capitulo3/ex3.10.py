salario = int(input("Digite seu salário: "))
porcentagem_aumento = int(input("Digite a porcentagem do aumento: "))
valor_aumento = salario * (porcentagem_aumento / 100)
salario_novo = salario + valor_aumento
print(f"O valor do aumento é de R$ {valor_aumento:.2f} e o novo salário é R$ {salario_novo:.2f} ")
