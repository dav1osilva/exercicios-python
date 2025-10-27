salário = float(input("Digite seu salário: "))
aumento = 0
if salário > 1250:
    aumento = salário * 0.10
if salário <= 1250:
    aumento = salário * 0.15
print(f"Com um salário de R$ {salário:.2f}, você terá um aumento de R$ {aumento:.2f}")
    