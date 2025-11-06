soma = 0

while True:
    n = int(input("Digite um número para somar ou 0 para encerrar: "))
    if n == 0:
        break
    else:
        soma += n

print(f"Soma = {soma}")