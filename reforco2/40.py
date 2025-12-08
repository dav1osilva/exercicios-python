capital_inicial = int(input("Digite o capital inicial: "))
capital = capital_inicial
taxa_juros = int(input("Digite a taxa de juros: "))
contador = 1

while contador <= 24:
    montante = capital + (capital * (taxa_juros / 100))
    print(f"Mês {contador} - R$ {montante:.2f}")
    capital = montante
    contador += 1

total = capital - capital_inicial
print(f"Total - R$ {total:.2f}")
