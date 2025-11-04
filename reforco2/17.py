n = int(input("Digite qualquer número para somar e 0 para encerrar: "))
soma = 0

while n != 0:
    soma += n
    n = int(input("Digite qualquer número para somar e 0 para encerrar: "))

print(f"soma = {soma}")