cigarros_por_dias = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Por quantos anos você já fumou? "))
anos_em_dias = anos * 365
tempo_perdido = int((cigarros_por_dias * 1 / 144) * anos_em_dias)
print(f"O tempo de vida perdido em dias por conta do cigarro é igual a {tempo_perdido}")