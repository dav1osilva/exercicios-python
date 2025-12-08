tamanho = int(input("Digite o lado do quadrado: "))
n1 = 1

while n1 <= tamanho:
    n2 = 1
    while n2 <= tamanho:
        print("*", end="")
        n2 += 1
    print("")
    n1 += 1
