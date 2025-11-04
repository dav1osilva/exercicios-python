senha = input("Digite a senha correta: ")
senha_correta = "ABC123"

while senha != senha_correta:
    print("Senha incorreta")
    senha = input("Digite a senha correta: ")

print("Acesso permitido")