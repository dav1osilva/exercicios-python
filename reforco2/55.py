soma = 0

while True:
    n = int(input("Digite um número: "))
    soma += n
    if soma > 100:
        break
print(f"A soma ultrapassou 100: total = {soma}")