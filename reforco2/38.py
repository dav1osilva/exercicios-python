n1 = int(input("Digite um número: "))
x = n1
n2 = int(input("Digite outro número: "))
quociente = 0

while x >= n2:
    quociente += 1
    x -= n2

print(f"{n1} / {n2} = {quociente}, resto = {x}")