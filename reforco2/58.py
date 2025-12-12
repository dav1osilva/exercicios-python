nome = input("Digite seu nome: ")
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))
notas = [n1, n2, n3]
p1, p2, p3 = 1, 2, 3
media_final = (n1 * p1 + n2 * p2 + n3 * p3) / 6
notas_ponderadas = [n1 * p1, n2 * p2, n3 * p3]
nota_mais_pesada = max(notas_ponderadas)

if n1 == n2 == n3:
    maior_nota = "Não há maior nota"
    menor_nota = "Não há menor nota"
else:
    maior_nota = max(notas)
    menor_nota = min(notas)

print(f"Média final = {media_final:.2f}\nmaior nota = {maior_nota}\nmenor nota = {menor_nota}\nnota mais pesada = {nota_mais_pesada}")