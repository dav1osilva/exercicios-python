n = int(input("Digite um número: "))
raiz_quadrada = n ** (1 / 2)
impar = 3

if n % 2 == 0 and n != 2:
    print(f"{n} não é primo")
else:
    while n % impar != 0 and impar <= raiz_quadrada:
        impar += 2
    if n % impar == 0:
        print(f"{n} não é primo")
    else:
        print(f"{n} é primo")
   