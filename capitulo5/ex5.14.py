contador = 0
soma = 0

while True:
    n = int(input("Digite um número para somar ou 0 para encerrar: "))
    if n == 0:
        break
    soma += n
    contador += 1

media = soma / contador
print(f"O número total de digítos foi igual a {contador}, a soma foi igual a {soma} e a média aritmética foi igual a {media}")

