dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = 0
n = dividendo

while n >= divisor:
    n -= divisor
    quociente += 1
resto = n

print(f"{dividendo} / {divisor} = {quociente}")
print(f"resto = {resto}")