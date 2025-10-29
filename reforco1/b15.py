valor = int(input("Digite o valor à sacar: "))

if valor % 100 == 0:
    notas = valor / 100
    print(f"{notas:.0f} nota(s) de R$ 100,00 serão sacadas")
if valor % 50 == 0:
    notas = valor / 50
    print(f"{notas:.0f} nota(s) de R$ 50,00 serão sacadas")
if valor % 20 == 0:
    notas = valor / 20
    print(f"{notas:.0f} nota(s) de R$ 20,00 serão sacadas")
if valor % 10 == 0:
    notas = valor / 10
    print(f"{notas:.0f} nota(s) de R$ 10,00 serão sacadas")
else:
    print("Você não sacará notas exatas") 