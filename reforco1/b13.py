nota = float(input("Digite sua nota: "))

if nota < 0 or nota > 10:
    print("As notas são dadas de 0 até 10")
elif nota < 5:
    print("D")
elif nota <= 6.9:
    print("C")
elif nota <= 8.9:
    print("B")
else:
    print("A")