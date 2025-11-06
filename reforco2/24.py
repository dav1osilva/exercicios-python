n = int(input("Digite um número: "))
divisor = n
quantidade_divisores = 0

while divisor > 0:
    resto = n % divisor
    divisor -= 1
    if resto == 0:
        quantidade_divisores += 1
    
if  quantidade_divisores > 2 or n == 1:
    print(f"{n} não é primo")
else:
    print(f"{n} é primo")