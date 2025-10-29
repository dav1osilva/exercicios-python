valor = float(input("Digite o valor do produto: "))

if valor <= 100:
    desconto = 0.05
else:
    desconto = 0.10

total = valor - (valor * desconto)

print(f"Com uma compra de R$ {valor:.2f}, você pagará apenas R$ {total:.2f}")

