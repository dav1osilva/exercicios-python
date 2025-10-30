dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
contador = dividendo
quociente = 0

while contador >= divisor:
    contador -= divisor
    quociente += 1

print(f"{dividendo} / {divisor} = {quociente}")
print(f"O resto será igual a {contador}")