senha = "python123"

while True:
    tentativa = input("Digite a senha: ")
    if tentativa == senha:
        break
    else:
        print("Acesso negado, tente novamente")

print("Acesso permitido")