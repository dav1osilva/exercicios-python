peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Normal")
elif imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")
    
