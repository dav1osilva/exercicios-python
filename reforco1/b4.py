nota = float(input("Digite sua nota: "))

if nota < 0 or nota > 10:
    print("As notas se limitam de 0 à 10")

elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")