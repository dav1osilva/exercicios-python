valor = int(input("Digite um valor: "))

notas_200 = valor // 200
valor -= notas_200 * 200

notas_100 = valor // 100
valor -= notas_100 * 100

notas_50 = valor // 50
valor -= notas_50 * 50

notas_20 = valor // 20
valor -= notas_20 * 20

notas_10 = valor // 10
valor -= notas_10 * 10

notas_5 = valor // 5
valor -= notas_5 * 5

notas_2 = valor // 2
valor -= notas_2 * 2


print(f"""
{notas_200} nota(s) de R$ 200
{notas_100} nota(s) de R$ 100
{notas_50} nota(s) de R$ 50
{notas_20} nota(s) de R$ 20
{notas_10} nota(s) de R$ 10
{notas_5} nota(s) de R$ 5
{notas_2} nota(s) de R$ 2
      """)