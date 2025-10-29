usuario = input("Qual é o usuário? ")
senha = input("Qual é a senha? ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido")
else:
    print("Acesso negado")