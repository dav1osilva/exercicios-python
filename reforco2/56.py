n = int(input("Digite a quantidade de segundos: "))

dias = n // 86400
n -= 86400 * dias
horas = n // 3600
n -= 3600 * horas
minutos = n // 60
n -= 60 * minutos
segundos = n 

print(f"{dias} dia(s), {horas} hora(s), {minutos} minuto(s), {segundos} segundo(s)")