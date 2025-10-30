capital_inicial = int(input("Depósito inicial: "))
taxa_juros = int(input("Taxa de juros: "))
deposito = int(input("Depósito mensal: "))
mes = 1
capital = capital_inicial

while mes <= 24:
    total = capital + (capital * taxa_juros / 100) + deposito
    print(f"Mês {mes} - R$ {total:.2f}")
    capital = total 
    mes += 1

juros = capital - capital_inicial    
print(f"O total obtido de juros foi igual a R$ {juros:.2f}")
