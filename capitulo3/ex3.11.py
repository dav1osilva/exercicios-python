preço = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual do desconto: "))
desconto = preço * (desconto / 100)
novo_preço = preço - desconto
print(f"O desconto é de R$ {desconto:.2f} e o novo preço é R$ {novo_preço:.2f}")