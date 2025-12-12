valor = int(input("Digite um valor: "))
notas = [200, 100, 50, 20, 10, 5, 2]

for nota in notas:
    quantidade = valor // nota
    print(f"{quantidade} nota(s) de R$ {nota}")
    valor = valor - (quantidade * nota)
    