divida_inicial = int(input("Dívida inicial: "))
juros = int(input("Juros: "))
divida = divida_inicial
cobranca_total = divida + (divida * juros / 100)
pagamento_mensal = int(input("Pagamento mensal: "))
pagamento_total = 0
meses = 0

while pagamento_total < cobranca_total:
    pagamento_total += pagamento_mensal
    meses += 1

print(f"O número de meses é igual a {meses}, o total pago será R$ {pagamento_total:.2f}")