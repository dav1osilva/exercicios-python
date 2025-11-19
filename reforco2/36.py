capital_inicial = int(input("Digite seu capital inicial: "))
taxa_juros = int(input("Digite a taxa de juros: "))
capital = capital_inicial
mes = 1

while mes <= 24:
    calculo = capital + (capital * (taxa_juros / 100))
    capital = calculo
    print(f"Mês {mes} - R$ {capital:.2f}")
    mes += 1

total = capital - capital_inicial
print(f"O total acumulado foi R$ {total:.2f}")
