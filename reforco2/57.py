nome = input("Digite o nome do aluno: ")
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))

nota_ponderada1 = n1 
nota_ponderada2 = n2 * 2
nota_ponderada3 = n3 * 3

# média ponderada
media_ponderada = (nota_ponderada1 + nota_ponderada2 + nota_ponderada3) / 6

# maior nota
if n1 == n2 == n3:
    maior_nota = "Não existe maior nota"
elif n1 > n2 and n1 > n3:
    maior_nota = n1
elif n2 > n1 and n2 > n3:
    maior_nota = n2
elif n3 > n1 and n3 > n2:
    maior_nota = n3        

# menor nota
if n1 == n2 == n3:
    menor_nota = "Não existe menor nota"
elif n1 < n2 and n1 < n3:
    menor_nota = n1
elif n2 < n1 and n2 < n3:
    menor_nota = n2
elif n3 < n1 and n3 < n2:
    menor_nota = n3        


# nota mais pesada
if nota_ponderada1 == nota_ponderada2 == nota_ponderada3:
    nota_pesada = "Não há maior nota"
elif nota_ponderada1 > nota_ponderada2 and nota_ponderada1 > nota_ponderada3:
    nota_pesada = nota_ponderada1
elif nota_ponderada2 > nota_ponderada1 and nota_ponderada2 > nota_ponderada3:
    nota_pesada = nota_ponderada2
elif nota_ponderada3 > nota_ponderada1 and nota_ponderada3 > nota_ponderada2:
    nota_pesada = nota_ponderada3         

print(f"Média final = {media_ponderada:.2f}, maior nota = {maior_nota}, menor nota = {menor_nota}, nota mais pesada = {nota_pesada}")