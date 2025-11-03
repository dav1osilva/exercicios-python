capital_inicial = float(input("Digite o capital inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))
mes = 1
capital = capital_inicial

while mes <= 24:
    juros_atual = capital + (capital * taxa_juros / 100)
    capital = juros_atual
    print(f"Mês {mes} - R$ {juros_atual:.2f} ")
    mes += 1

total = capital - capital_inicial    
print(f"Total - R$ {total:.2f}")