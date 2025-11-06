import random
resposta = random.randint(1, 10)

while True:
    tentativa = int(input("Digite um número de 1 à 10: "))
    if tentativa == resposta:
        break
    else:
        print("Resposta incorreta, tente novamente")

print("Você acertou a resposta!")