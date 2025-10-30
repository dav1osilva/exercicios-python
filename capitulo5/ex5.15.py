codigos = [1, 2, 3, 5, 9]
preco = 0
quantidade = 0
total = 0

while True:
    n = int(input("Digite o código: "))
    if n == 0:
        break
    elif n not in codigos:
        print("Código inválido")
    else:
        if n == 1:
            preco = 0.50
        elif n == 2:
            preco = 1
        elif n == 3:
            preco = 4
        elif n == 5:
            preco = 7
        elif n == 9:
            preco = 8
    quantidade = int(input("Digite a quantidade: "))
    total += quantidade * preco

    
print(f"O total será igual a R$ {total:.2f}")



            
