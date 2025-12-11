import random

resposta = random.randint(1, 100)

while True:
    tentativa = int(input("Escolha um número de 1 à 100: "))
    if tentativa == resposta:
        print("Você acertou!")
        break
    elif tentativa < resposta:
        print("A resposta é um número maior")
    else:
        print("A resposta é um número menor")
    print("Tente novamente :(")
        