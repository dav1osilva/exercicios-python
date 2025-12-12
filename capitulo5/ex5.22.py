while True:
    operacao = input("Escolha uma operação: +, -, *, / ou digite sair para encerrar ")
    if operacao == "sair":
        break
    n1 = 1
    while n1 <= 10:
        n2 = 1
        while n2 <= 10:
            if operacao == "+":
                print(f"{n1} + {n2} = {n1 + n2}")
            elif operacao == "-":
                print(f"{n1} - {n2} = {n1 - n2}")
            elif operacao == "*":
                print(f"{n1} * {n2} = {n1 * n2}")
            elif operacao == "/":
                print(f"{n1} / {n2} = {n1 / n2}")
            n2 += 1
        print()    
        n1 += 1
    else:
        print("Opção não encontrada")