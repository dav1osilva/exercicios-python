km = float(input("Quantos km você deseja percorrer? "))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print(f"Em um percurso de {km} km, você pagará um total de R$ {preço:.2f}")