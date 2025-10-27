velocidade = float(input("Qual foi a velocidade média do seu carro? "))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print(f"Você será multado por excesso de velocidade, e a multa será de R$ {multa:.2f}")