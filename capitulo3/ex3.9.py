dias = int(input("Quantos dias: "))
horas = int(input("Quantas horas: "))
minutos = int(input("Quantos minutos: "))
segundos = int(input("Quantos segundos: "))
total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"Isso resulta em um total de {total} segundos")