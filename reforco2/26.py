import random

resposta = random.randint(1, 100)
n = int(input("Digite um número: "))

while n != resposta:
    if n > resposta:
        print(f"A resposta certa é menor que {n}")
    else:
        print(f"A resposta certa é maior que {n}")
    n = int(input("Digite um número: "))
    
print(f"{resposta} é a resposta certa!")